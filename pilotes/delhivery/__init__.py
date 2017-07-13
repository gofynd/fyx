"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
.. note::
    This file contains the Base class which will set the client name and api token for making the delhivery API calls
"""


import logging
import requests

from user_profile import UserProfile
from constants import DELHIVERY_CREATE_PACKAGE_HEADERS
from response_handler import ResponseHandler


class DelhiveryBase(object):
    """This class contains the abstract methods that
    are needed for preparing request and response for
    making calls Delhivery.
    """

    def __init__(self, user_profile):
        """Initialization method for Delhivery base class, which sets
        credentials for using Delhivery API

        Args:
            user_profile - This will be the dictionary containing
            client name and api token.
        """
        self.prepared_data = None
        self.url = None
        self.method = 'GET'
        self.headers = {}
        self.profile = UserProfile(**user_profile)
        self.logger = logging.getLogger(__name__)
        self.response = ResponseHandler({"success": False, "ok": False, "content": ''})

    def _prepare_pre_request_data(self):
        """This is abstract method and have to be over ridden in subclass.
        Inside subclass it will prepare the data for request.

        Args:
            data - It contains the payload needed for the API Call
        :return: None
        """
        pass

    def _prepare_response(self):
        """This is abstract method and have to be over ridden in subclass.
        This will prepare response accordingly.

        Args:
            None

        :return: None
        """
        pass

    def send_request(self):
        """
        Used to send the final JSON response and to be called by subclass.
        It internally override the _send_request of subclass.

        :return: Response
        """
        try:
            self._prepare_pre_request_data()
            if self.method == 'GET':
                self.response = requests.get(self.url)
            else:
                self.response = requests.post(self.url, data=self.prepared_data, headers=self.headers, timeout=14)

        except Exception as exc:
            self.logger.exception(exc)

        self._prepare_response()
        return self.response
