"""
File: services
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

It contains all the core service methods required for the delhivery.
"""
from . import EcommBase
from hedwig.settings import ECOM_BASE_URL
from constants import ECOM_PLACE_SHIPMENT, ECOM_CANCEL_SHIPMENT
from helper import ECOMXMLParser


class CreatePackage(EcommBase):

    """
    Create the new shipment in Ecomm.
    """
    def __init__(self, user_profile):
        super(CreatePackage, self).__init__(user_profile)

    def _prepare_pre_request_data(self, data):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.prepared_data = data
        self.url = ECOM_BASE_URL + ECOM_PLACE_SHIPMENT
        self.prepared_data['username'] = self.profile.username
        self.prepared_data['password'] = self.profile.password
        self.method = 'POST'
        self.logger.info("Payload received for creating package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        if self.response:
            self.response = self.response.json()


class CancelShipment(EcommBase):
    def __init__(self, user_profile):
        super(CancelShipment, self).__init__(user_profile)

    def _prepare_pre_request_data(self, data):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        :return:
        """
        self.prepared_data = data
        self.url = ECOM_BASE_URL + ECOM_CANCEL_SHIPMENT
        self.method = 'POST'
        self.logger.info("Payload received to cancel package\n{}".format(self.prepared_data))

    def _prepare_response(self):
        """
        This method is overridden.
        Prepare response in json.
        :return: None
        """
        formatted_response = {}
        if self.response and self.response.ok:
            json_response = self.response.json()
            formatted_response = json_response[0]
        else:
            formatted_response['status'] = 'False'
        self.response = formatted_response

