"""
File: services
Author: Om Prakash <omprakash@gofynd.com>
Date: 10/02/2017

It contains all the core service classes required for the bluedart.
"""

from pilotes.bluedart import BlueDart
from pilotes.bluedart.user_profile import UserProfile
from constants import BLUEDART_BASE_URL, BLUEDART_DEBUG_BASE_URL


class CreateShipment(BlueDart):
    """
    Create the new shipment in bluedart.
    """

    def __init__(self, profile_creds):
        request_url = BLUEDART_BASE_URL + 'WayBill/WayBillGeneration.svc?wsdl'
        if profile_creds.get('debug', False):
            request_url = BLUEDART_DEBUG_BASE_URL + 'WayBill/WayBillGeneration.svc?wsdl'
        self.request = None
        self.profile = None
        self.consignee = None
        self.shipper = None
        self.services = None
        self.user_profile = UserProfile(**profile_creds)
        super(CreateShipment, self).__init__(request_url)

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
