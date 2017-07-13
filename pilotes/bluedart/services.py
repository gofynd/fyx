"""
File: services
Author: Om Prakash <omprakash@gofynd.com>
Date: 10/02/2017

It contains all the core service classes required for the bluedart.
"""

from pilotes.bluedart import BlueDart
from pilotes.bluedart.user_profile import UserProfile
from constants import BLUEDART_BASE_URL, BLUEDART_DEBUG_BASE_URL, SHIPMENT_TYPE


class CreateShipment(BlueDart):
    """
    Create the new shipment in bluedart.
    """

    def __init__(self, profile_creds, data):
        request_url = BLUEDART_BASE_URL + 'WayBill/WayBillGeneration.svc?wsdl'
        if profile_creds.get('debug', False):
            request_url = BLUEDART_DEBUG_BASE_URL + 'WayBill/WayBillGeneration.svc?wsdl'
        self.request = None
        self.profile = None
        self.consignee = None
        self.shipper = None
        self.services = None
        self.data = data
        self.user_profile = UserProfile(**profile_creds)
        super(CreateShipment, self).__init__(request_url, data)

    def _create_request_payload(self):
        # Finding AWB type
        awb_type = "Prepaid"
        if self.data["shipment_type"] == SHIPMENT_TYPE['cod']:
            awb_type = "COD"

        cod_val = self.data['product_cod_value'] if awb_type == SHIPMENT_TYPE['cod'] else 0
        pickup_date = self.data['pickup_date']

        # Consignee Details
        # ToDO: Om PLease check on the bluedart address guidelines so we can add them on our side.
        self.consignee = self.Consignee(
            ConsigneeName=self.data['consignee_name'],
            ConsigneeMobile=self.data['consignee_mobile'],
            ConsigneeAddress1=self.data['consignee_address1'],
            ConsigneeAddress2=self.data['consignee_city'],
            ConsigneeAddress3=self.data['consignee_state'],
            ConsigneePincode=self.data['consignee_pincode'],
            ConsigneeTelephone=self.data.get('consignee_phone', "")
        )

        # Shipper Details.
        address3 = '%s, %s' % (self.data['pickup_city'], self.data['pickup_state'])

        # TODO - Check on validations for address length -- only for bluedart
        self.shipper = self.Shipper(
            # TODO - Need to move customer_name into user profile
            # CustomerName=self.user_profile.customer_name,
            CustomerAddress1=self.data.get('pickup_address1', ""),
            CustomerAddress2=self.data.get('pickup_address2', ""),
            CustomerAddress3=address3,
            CustomerCode=self.user_profile.customer_code,
            OriginArea=self.data['origin_area_code'],
            # TODO - Need to move sender into user profile
            # Sender=self.user_profile.sender,
            CustomerPincode=self.data['pickup_pincode'],
            CustomerMobile=self.data['pickup_phone'],
            CustomerTelephone="",
        )

        commodity = self.Commodity(
            CommodityDetail1=self.data['product_category'],
            CommodityDetail2=self.data['product_name'],
            CommodityDetail3=self.data['product_brand'],
        )

        # Shipping Item Details
        dimensions = self.dimension(
            Breadth=self.data['breadth'],
            Height=self.data['height'],
            Length=self.data['length'],
            Count=self.data['quantity']
        )
        self.services = self.Services(
            ActualWeight=self.data['weight'],
            CollectableAmount=cod_val,
            CreditReferenceNo=self.data['shipment_number'],
            DeclaredValue=self.data['product_value'],
            # need here a unique key must be added to docs
            # InvoiceNo=self.data[''],
            PickupTime=self.data['pickup_time'],
            PieceCount=self.data['quantity'],
            # TODO - BLUEDART PRODUCT DETAILS NEEDED TO BE TAKEN AT THE TIME OF INITIALISATION. PLease CHECK OM
            # ProductCode=BLUEDART_PRODUCT_DETAILS['apex'],
            # ProductType=BLUEDART_PRODUCT_DETAILS['type'],
            SubProductCode="C" if awb_type == SHIPMENT_TYPE['cod'] else "P",
            Commodity=commodity,
            Dimensions=[dimensions],
            PickupDate=pickup_date,
            RegisterPickup=True
        )

    def _prepare_pre_request_data(self):
        """
        Prepare pre request WSDL prefixes.
        """
        self.Request = self.client.get_element('ns2:WayBillGenerationRequest')
        self.Profile = self.client.get_element('ns4:UserProfile')
        self.Consignee = self.client.get_element("ns2:Consignee")
        self.Shipper = self.client.get_element("ns2:Shipper")
        self.Services = self.client.get_element("ns2:Services")
        self.Commodity = self.client.get_element("ns2:CommodityDetail")
        self.dimension = self.client.get_element("ns2:Dimension")
        self._create_request_payload()
        self.profile = self._set_profile_credentials(self.user_profile)

    def _send_request(self):
        """
        Call GenerateWayBill.
        """
        response = {}
        try:
            self.request = self.Request(
                Consignee=self.consignee,
                Shipper=self.shipper,
                Services=self.services
            )
            response = self.client.service.GenerateWayBill(self.request, self.profile)
        except Exception as exc:
            response["message"] = str(exc)

        return response


class CreatePickup(BlueDart):
    """
    This Class to register pickup request for bluedart.
    It extends the Parent class BlueDart.
    """

    def __init__(self, profile_creds):
        request_url = BLUEDART_BASE_URL + "Pickup/PickupRegistrationService.svc?wsdl"
        if profile_creds.get('debug', False):
            request_url = BLUEDART_DEBUG_BASE_URL + "Pickup/PickupRegistrationService.svc?wsdl"
        self.Request = None
        self.data_request = None
        self.data_profile = None
        self.user_profile = UserProfile(**profile_creds)
        super(CreatePickup, self).__init__(request_url)

    def _prepare_pre_request_data(self):
        """
        Prepare pre request WSDL prefixes.
        :return: None
        """
        self.Request = self.client.get_element('ns2:PickupRegistrationRequest')
        self.Profile = self.client.get_element('ns6:UserProfile')
        self.data_profile = self._set_profile_credentials(self.user_profile)

    def _send_request(self):
        """
        Send request to RegisterPickup.
        :return: response from SOAP server.
        """
        return self.client.service.RegisterPickup(self.data_request, self.data_profile)


class CancelShipment(BlueDart):
    """
    Cancel a already registered shipment request in bluedart.
    It extends the Parent class BlueDart.
    """

    def __init__(self, profile_creds):
        request_url = BLUEDART_BASE_URL + "WayBill/WayBillGeneration.svc?wsdl"
        if profile_creds.get('debug', False):
            request_url = BLUEDART_DEBUG_BASE_URL + "WayBill/WayBillGeneration.svc?wsdl"
        self.Request = None
        self.request = None
        self.profile = None
        self.awb_no = ''
        self.user_profile = UserProfile(**profile_creds)
        super(CancelShipment, self).__init__(request_url)

    def _prepare_pre_request_data(self):
        """
        Prepare pre request WSDL params.
        :return: None
        """
        self.Request = self.client.get_element('ns2:AWBCancelationRequest')
        self.Profile = self.client.get_element('ns4:UserProfile')
        self.profile = self._set_profile_credentials(self.user_profile)

    def _send_request(self):
        """
        Send request to CancelWaybill.
        :return: response from SOAP server.
        """
        response = {}
        try:
            if self.awb_no:
                self.request = self.Request(AWBNo=self.awb_no)
            response = self.client.service.CancelWaybill(self.request, self.profile)

        except Exception as exc:
            response["message"] = str(exc)

        return response
