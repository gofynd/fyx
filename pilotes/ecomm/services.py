"""
File: services
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

It contains all the core service methods required for the delhivery.
"""
import json

from pilotes.ecomm import EcommBase
from constants import ECOM_PLACE_SHIPMENT, ECOM_CANCEL_SHIPMENT, ECOM_BASE_URL, ECOM_DEBUG_BASE_URL, \
    ECOM_FETCH_AWBS, AWB_COUNT_FROM_CREATE_SHIPMENT


class CreateShipment(EcommBase):

    """
    Create the new shipment in Ecomm.
    """
    def __init__(self, user_profile):
        self.user_profile = user_profile
        super(CreateShipment, self).__init__(user_profile)
        self.prepared_data = dict()

    def _prepare_pre_request_data(self, data):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.url = ECOM_BASE_URL + ECOM_PLACE_SHIPMENT
        if self.profile.debug:
            self.url = ECOM_DEBUG_BASE_URL + ECOM_PLACE_SHIPMENT
        create_awb = CreateAWB(self.user_profile, data['awb_type'])
        awb_data = create_awb.send_request(AWB_COUNT_FROM_CREATE_SHIPMENT)
        self.prepared_data = dict()
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password
        if isinstance(awb_data.get('awb'), list):
            data['AWB_NUMBER'] = awb_data['awb'][0]
        self.prepared_data["json_input"] = json.dumps([data])
        self.method = 'POST'
        self.logger.info("Payload received for creating package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        try:
            if self.response:
                self.response = self.response.json()
        except:
            self.response = {}


class CancelShipment(EcommBase):
    def __init__(self, user_profile):
        super(CancelShipment, self).__init__(user_profile)
        self.prepared_data = dict()


    def _prepare_pre_request_data(self, awbs):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        if isinstance(awbs, list):
            self.prepared_data["awbs"] = ",".join(awbs)
        elif isinstance(awbs, str):
            self.prepared_data["awbs"] = awbs
        elif isinstance(awbs, int):
            self.prepared_data["awbs"] = str(awbs)

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
    def __init__(self, user_profile, awb_type):
        super(CreateAWB, self).__init__(user_profile)
        self.awb_type = awb_type
        self.prepared_data = dict()

    def _prepare_pre_request_data(self, count):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password
        self.prepared_data['count'] = count
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
