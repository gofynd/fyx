"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
.. note::
    It contains all the core service methods required for the delhivery.
"""

from . import DelhiveryBase
from constants import DELHIVERY_CREATE_PACKAGE, DELHIVERY_CANCEL_PACKAGE, DELHIVERY_CREATE_PICKUP, \
    DELHIVERY_CREATE_PACKAGE_HEADERS, DELHIVERY_CANCEL_PACKAGE_HEADERS, DELHIVERY_BASE_URL, DELHIVERY_DEBUG_BASE_URL
from helper import DelhiveryXMLHelper


class CreatePackage(DelhiveryBase):

    """
    Create the new shipment in delhivery.
    """

    def __init__(self, user_profile):
        super(CreatePackage, self).__init__(user_profile)

    def _prepare_pre_request_data(self, data):

        """Prepare data for request.
        TODO: Serialization to be added.
        Args:
            data - The data that will be prepared before sending it to Delhivery
        :return:
            None
        """

        self.prepared_data = data
        self.url = DELHIVERY_BASE_URL + DELHIVERY_CREATE_PACKAGE.format(self.profile.api_token)
        if self.profile.debug:
            self.url = DELHIVERY_DEBUG_BASE_URL + DELHIVERY_CREATE_PACKAGE.format(self.profile.api_token)
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

    def _prepare_pre_request_data(self, data):

        """
        Prepare data for request.
        TODO: Serialization to be added.
        Args:
            data - The data that will be prepared before sending it to Delhivery
        :return:
            None
        """

        self.prepared_data = data
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
