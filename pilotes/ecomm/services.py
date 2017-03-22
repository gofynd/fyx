"""
File: services
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

It contains all the core service methods required for the delhivery.
"""
import json

from pilotes.ecomm import EcommBase
from constants import ECOM_PLACE_SHIPMENT, ECOM_CANCEL_SHIPMENT, ECOM_BASE_URL, ECOM_DEBUG_BASE_URL, ECOM_FETCH_AWBS


class CreateShipment(EcommBase):

    """
    Create the new shipment in Ecomm.
    """
    def __init__(self, user_profile):
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
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password

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
        self.prepared_data = dict()
        super(CancelShipment, self).__init__(user_profile)

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
    def __init__(self, user_profile, awb_type='COD'):
        self.awb_type = awb_type
        self.prepared_data = dict()
        super(CreateAWB, self).__init__(user_profile)

    def _prepare_pre_request_data(self, awbs):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password
        self.prepared_data['count'] = 1
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
