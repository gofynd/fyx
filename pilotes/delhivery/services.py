"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
.. note::
    It contains all the core service methods required for the delhivery.
"""
import json

from pilotes.delhivery import DelhiveryBase
from constants import DELHIVERY_CREATE_PACKAGE, DELHIVERY_CANCEL_PACKAGE, DELHIVERY_CREATE_PICKUP, \
    DELHIVERY_CREATE_PACKAGE_HEADERS, DELHIVERY_CANCEL_PACKAGE_HEADERS, DELHIVERY_BASE_URL,\
    DELHIVERY_DEBUG_BASE_URL, DELHIVERY_FETCH_BULK_AWB, AWB_COUNT_FROM_CREATE_SHIPMENT, DELHIVERY_DATA_FORMAT, \
    SHIPMENT_TYPE
from helper import DelhiveryXMLHelper


class CreateShipment(DelhiveryBase):

    """
    Create the new shipment in delhivery.
    """

    def __init__(self, user_profile, data):
        self.user_profile = user_profile
        self.data = data
        self.payload = dict()
        super(CreateShipment, self).__init__(user_profile)

    def _create_request_payload(self):
        self.payload['waybill'] = self.data.get('awb_num', None)
        self.payload['order'] = self.data['shipment_number']
        self.payload['products_desc'] = self.data['product_name']
        self.payload['order_date'] = self.data['order_date']  # It must be iso string format. Need to be mentioned in docs
        self.payload['payment_mode'] = SHIPMENT_TYPE[self.data['shipment_type']]
        self.payload['total_amount'] = self.data['product_cod_value']
        self.payload['cod_amount'] = self.data['product_cod_value'] if self.payload['payment_mode'] == SHIPMENT_TYPE['cod'] else 0.0

        # Customer info
        self.payload['name'] = self.data['consignee_name']
        self.payload['phone'] = self.data['consignee_phone']
        self.payload['add'] = self.data['consignee_address1'] + " " + self.data['consignee_address2']
        self.payload['city'] = self.data['consignee_city']
        self.payload['state'] = self.data['consignee_state']
        self.payload['country'] = self.data['consignee_country']
        self.payload['pin'] = self.data['consignee_pincode']

        # If Undelivered Return Address
        self.payload['return_name'] = self.data['rto_name']
        self.payload['return_phone'] = self.data['rto_phone']
        self.payload['return_add'] = self.data['rto_address1'] + " " + self.data['rto_address1']
        self.payload['return_pin'] = self.data['rto_pincode']
        self.payload['return_city'] = self.data['rto_city']
        self.payload['return_state'] = self.data['rto_state']
        self.payload['return_country'] = self.data['rto_country']
        self.payload['code'] = self.data['warehouse_code']

        # Extra Required Fields
        self.payload['supplier'] = self.payload['return_name']
        self.payload['weight'] = self.data['weight']
        self.payload['billable_weight'] = self.payload['weight']
        self.payload['dimensions'] = "{}CM x {}CM x {}CM".format(self.data['length'], self.data['breadth'], self.data['height'])
        self.payload['volumetric'] = 0.0
        self.payload['quantity'] = self.data['quantity']

        # Setting pickup location parameters according to new API
        # self.pickup_parameters['address'] = payload['bags'][0]['store']['address1']
        # self.pickup_parameters['city'] = payload['bags'][0]['store']['city']
        # self.pickup_parameters['country'] = payload['bags'][0]['store']['country']
        # self.pickup_parameters['name'] = self.data['warehouse_name']  # Name as registered with Delhivery
        # self.pickup_parameters['phone'] = re.sub(r'\s+', '', store_phone_number)
        # self.pickup_parameters['pin'] = payload['bags'][0]['store']['pincode']

        # Seller Info
        self.payload['seller_name'] = self.payload['return_name']
        self.payload['seller_add'] = self.payload['return_add']

        # GST Info
        if self.data.get("seller_gst_number"):
            self.payload['seller_gst_tin'] = self.data['seller_gst_number']

    def _prepare_pre_request_data(self):

        """Prepare data for request.
        TODO: Serialization to be added.
        Args:
            data - The data that will be prepared before sending it to Delhivery
        :return:
            None
        """
        self._create_request_payload()
        self.url = DELHIVERY_BASE_URL + DELHIVERY_CREATE_PACKAGE.format(self.profile.api_token)
        if self.profile.debug:
            self.url = DELHIVERY_DEBUG_BASE_URL + DELHIVERY_CREATE_PACKAGE.format(self.profile.api_token)
        # We Will create AWB only if not found in payload.
        if not self.payload['waybill']:
            create_awb = CreateAWB(self.user_profile,  None, AWB_COUNT_FROM_CREATE_SHIPMENT)
            awb_data = create_awb.send_request()
            self.data['waybill'] = awb_data
        self.prepared_data = dict()
        self.prepared_data['data'] = json.dumps({"shipments": [self.payload]})
        self.prepared_data['format'] = DELHIVERY_DATA_FORMAT
        self.method = 'POST'
        self.headers = DELHIVERY_CREATE_PACKAGE_HEADERS
        self.logger.info("Payload received for creating package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        """Prepare response that will be returned to caller.
        Args:
            None
        :return:
            None
        """

        if self.response:
            self.response = self.response.json()


class CancelShipment(DelhiveryBase):
    """Cancels the previously created shipment in delhivery.
    """

    def __init__(self, user_profile, data):
        super(CancelShipment, self).__init__(user_profile)
        self.data = data
        self.prepared_data = dict()

    def _prepare_pre_request_data(self):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        Args:
            data - The data that will be prepared before sending it to Delhivery
        :return:
            None
        """
        self.prepared_data['waybill'] = self.data['waybill']
        self.prepared_data['cancellation'] = True
        self.prepared_data['format'] = DELHIVERY_DATA_FORMAT
        self.url = DELHIVERY_BASE_URL + DELHIVERY_CANCEL_PACKAGE
        if self.profile.debug:
            self.url = DELHIVERY_DEBUG_BASE_URL + DELHIVERY_CANCEL_PACKAGE
        self.method = 'POST'
        self.headers['Authorization'] = DELHIVERY_CANCEL_PACKAGE_HEADERS['Authorization'].format(self.profile.api_token)
        self.logger.info("Payload received to cancel package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        """
        This method is overridden.
        Prepare response in json.
        Args:
            None
        :return:
            None
        """

        formatted_response = {}
        if self.response:
            xml_response = self.response.content
            formatted_response = DelhiveryXMLHelper(xml_response).parse()
            if not formatted_response.get('status'):
                formatted_response['status'] = 'False'
        self.response = formatted_response


class CreatePickup(DelhiveryBase):
    def __init__(self, user_profile, data):
        self.data = data
        super(CreatePickup, self).__init__(user_profile)

    def _prepare_pre_request_data(self):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """

        self.prepared_data = self.data
        self.url = DELHIVERY_BASE_URL + DELHIVERY_CREATE_PICKUP
        if self.profile.debug:
            self.url = DELHIVERY_DEBUG_BASE_URL + DELHIVERY_CREATE_PICKUP
        self.method = 'POST'
        self.headers = DELHIVERY_CREATE_PACKAGE_HEADERS
        self.logger.info("Payload received for creating pickup\n{}".format(self.prepared_data))

    def _prepare_response(self):
        """
        This method is overridden.
        Prepare response in json.
        Args:
            None
        :return:
            None
        """

        if self.response.ok:
            formatted_response = self.response.json()
            formatted_response['success'] = True
        else:
            formatted_response = self.response.json()
            formatted_response['success'] = False

        self.response = formatted_response


class CreateAWB(DelhiveryBase):
    # Delhivery do not differentiate between COD and PREPAID as ecomm does.
    def __init__(self, user_profile, awb_type, count):
        self.count = count
        self.awb_type = awb_type
        self.prepared_data = dict()
        super(CreateAWB, self).__init__(user_profile)

    def _prepare_pre_request_data(self):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        delhivery_fetch_bulk_awb = DELHIVERY_FETCH_BULK_AWB.format(self.profile.client_name, self.count,
                                                                   self.profile.api_token)
        self.url = DELHIVERY_BASE_URL + delhivery_fetch_bulk_awb
        if self.profile.debug:
            self.url = DELHIVERY_DEBUG_BASE_URL + delhivery_fetch_bulk_awb
        self.method = 'GET'
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
        except Exception as ex:
            self.logger.exception(ex)
            self.response = {}
