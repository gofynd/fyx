"""
File: services
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

It contains all the core service methods required for the delhivery.
"""
import json

from pilotes.ecomm import EcommBase
from constants import ECOM_PLACE_SHIPMENT, ECOM_CANCEL_SHIPMENT, ECOM_BASE_URL, ECOM_DEBUG_BASE_URL, \
    ECOM_FETCH_AWBS, AWB_COUNT_FROM_CREATE_SHIPMENT, SHIPMENT_TYPE


class CreateShipment(EcommBase):

    """
    Create the new shipment in Ecomm.
    """
    def __init__(self, user_profile, data):
        self.data = data
        self.user_profile = user_profile
        self.awb_type = SHIPMENT_TYPE['pre-paid']
        self.payload = dict()
        super(CreateShipment, self).__init__(user_profile)
        self.prepared_data = dict()

    def _create_request_payload(self):
        # Required Parameter
        self.awb_type = SHIPMENT_TYPE['pre-paid']
        self.payload['COLLECTABLE_VALUE'] = 0
        if self.data["shipment_type"] == SHIPMENT_TYPE['cod']:
            self.awb_type = "COD"
            self.payload['COLLECTABLE_VALUE'] = self.data['product_cod_value']

        # Order info
        self.payload['ORDER_NUMBER'] = self.data['shipment_number']
        self.payload['AWB_NUMBER'] = self.data.get('awb_num', None)

        # Item info
        self.payload['PRODUCT'] = self.awb_type
        self.payload['ITEM_DESCRIPTION'] = self.data['product_name']
        self.payload['DECLARED_VALUE'] = self.data['product_cod_value']
        self.payload['ACTUAL_WEIGHT'] = str(self.data['weight'])

        # Customer info
        self.payload['CONSIGNEE'] = self.data['consignee_name']
        self.payload['MOBILE'] = self.data['consignee_mobile']
        self.payload['TELEPHONE'] = self.data['consignee_phone']
        self.payload['CONSIGNEE_ADDRESS1'] = self.data['consignee_address1']
        self.payload['CONSIGNEE_ADDRESS2'] = self.data['consignee_address2']
        self.payload['DESTINATION_CITY'] = self.data['consignee_city']
        self.payload['STATE'] =  self.data['consignee_state']
        self.payload['PINCODE'] = self.data['consignee_pincode']

        # Extra Required Fields
        self.payload['CONSIGNEE_ADDRESS3'] = " "
        self.payload['PIECES'] = self.data['quantity']
        self.payload['VOLUMETRIC_WEIGHT'] = str(self.data['weight'])
        self.payload['LENGTH'] = self.data['length']
        self.payload['BREADTH'] = self.data['breadth']
        self.payload['HEIGHT'] = self.data['height']

        # Pick up info
        self.payload['PICKUP_NAME'] = self.data['pickup_name']
        self.payload['PICKUP_MOBILE'] = self.data['pickup_mobile']
        self.payload['PICKUP_PHONE'] = self.data['pickup_phone']
        self.payload['PICKUP_ADDRESS_LINE1'] = self.data['pickup_address1']
        self.payload['PICKUP_ADDRESS_LINE2'] = self.data['pickup_address2']
        self.payload['PICKUP_PINCODE'] = str(self.data['pickup_pincode'])

        # If undelivered Return to address info
        self.payload['RETURN_NAME'] = self.data['rto_name']
        self.payload['RETURN_MOBILE'] = self.data['rto_mobile']
        self.payload['RETURN_PHONE'] = self.data['rto_phone']
        self.payload['RETURN_ADDRESS_LINE1'] = self.data['rto_address1']
        self.payload['RETURN_ADDRESS_LINE2'] = self.data['rto_address2']
        self.payload['RETURN_PINCODE'] = str(self.data['rto_pincode'])
        # SELLER_GSTIN is not mandatory for ECOMM
        if self.data.get('seller_gst_number'):
            self.payload['SELLER_GSTIN'] = self.data['seller_gst_number']

    def _prepare_pre_request_data(self):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self._create_request_payload()
        self.url = ECOM_BASE_URL + ECOM_PLACE_SHIPMENT
        if self.profile.debug:
            self.url = ECOM_DEBUG_BASE_URL + ECOM_PLACE_SHIPMENT
        if not self.data.get('awb_num', None):
            create_awb = CreateAWB(self.user_profile, self.awb_type, AWB_COUNT_FROM_CREATE_SHIPMENT)
            awb_data = create_awb.send_request()
            if isinstance(awb_data.get('awb'), list):
                self.payload['AWB_NUMBER'] = awb_data['awb'][0]
        self.prepared_data = dict()
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password

        self.prepared_data["json_input"] = json.dumps([self.payload])
        self.method = 'POST'
        self.logger.info("Payload received for creating package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        try:
            if self.response:
                self.response = self.response.json()
        except:
            self.response = {}


class CancelShipment(EcommBase):
    def __init__(self, user_profile, data):
        self.data = data
        super(CancelShipment, self).__init__(user_profile)
        self.prepared_data = dict()

    def _prepare_pre_request_data(self):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.prepared_data["awbs"] = str(self.data['waybill'])
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password
        self.url = ECOM_BASE_URL + ECOM_CANCEL_SHIPMENT
        if self.profile.debug:
            self.url = ECOM_DEBUG_BASE_URL + ECOM_CANCEL_SHIPMENT
        self.method = 'POST'
        self.logger.info("Payload received to cancel package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        """
        This method is overridden.
        Prepare response in json.
        :return: None
        """
        formatted_response = {}
        try:
            if self.response and self.response.ok:
                json_response = self.response.json()
                formatted_response = json_response[0]
            else:
                formatted_response['status'] = 'False'
            self.response = formatted_response
        except:
            self.response = {}


class CreateAWB(EcommBase):
    # Two allowed values for AWB Type are COD and PPD
    def __init__(self, user_profile, awb_type, data):
        super(CreateAWB, self).__init__(user_profile)
        self.awb_type = awb_type
        self.count = data
        self.prepared_data = dict()

    def _prepare_pre_request_data(self):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password
        self.prepared_data['count'] = self.count
        self.prepared_data['type'] = self.awb_type
        self.url = ECOM_BASE_URL + ECOM_FETCH_AWBS
        if self.profile.debug:
            self.url = ECOM_DEBUG_BASE_URL + ECOM_FETCH_AWBS
        self.method = 'POST'
        self.logger.info("Payload received to create AWB numbers\n{}".format(self.prepared_data))

    def _prepare_response(self):
        """
        This method is overridden.
        Prepare response in json.
        :return: None
        """
        formatted_response = {}
        try:
            if self.response and self.response.ok:
                json_response = self.response.json()
                formatted_response = json_response
            else:
                formatted_response['status'] = 'False'
            self.response = formatted_response
        except:
            self.response = {}
