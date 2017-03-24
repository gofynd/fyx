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
    DELHIVERY_DEBUG_BASE_URL, DELHIVERY_FETCH_BULK_AWB, AWB_COUNT_FROM_CREATE_SHIPMENT, DELHIVERY_DATA_FORMAT
from helper import DelhiveryXMLHelper


class CreateShipment(DelhiveryBase):

    """
    Create the new shipment in delhivery.
    """

    def __init__(self, user_profile):
        self.user_profile = user_profile
        super(CreateShipment, self).__init__(user_profile)

    def _prepare_pre_request_data(self, data):

        """Prepare data for request.
        TODO: Serialization to be added.
        Args:
            data - The data that will be prepared before sending it to Delhivery
        :return:
            None
        """

        self.url = DELHIVERY_BASE_URL + DELHIVERY_CREATE_PACKAGE.format(self.profile.api_token)
        if self.profile.debug:
            self.url = DELHIVERY_DEBUG_BASE_URL + DELHIVERY_CREATE_PACKAGE.format(self.profile.api_token)
        create_awb = CreateAWB(self.user_profile, None)
        awb_data = create_awb.send_request(AWB_COUNT_FROM_CREATE_SHIPMENT)
        self.prepared_data = dict()
        data['waybill'] = awb_data
        self.prepared_data['data'] = json.dumps({"shipments": [data]})
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

    def __init__(self, user_profile):
        super(CancelShipment, self).__init__(user_profile)
        self.prepared_data = dict()

    def _prepare_pre_request_data(self, data):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        Args:
            data - The data that will be prepared before sending it to Delhivery
        :return:
            None
        """
        self.prepared_data['waybill'] = data['waybill']
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
    def __init__(self, user_profile):
        super(CreatePickup, self).__init__(user_profile)

    def _prepare_pre_request_data(self, data):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """

        self.prepared_data = data
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
    def __init__(self, user_profile, awb_type):
        self.awb_type = awb_type
        self.prepared_data = dict()
        super(CreateAWB, self).__init__(user_profile)

    def _prepare_pre_request_data(self, count):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        delhivery_fetch_bulk_awb = DELHIVERY_FETCH_BULK_AWB.format(self.profile.client_name, count,
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
