"""
File: Base class
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

This file contains the Base class which will set the client name and api token for making the delhivery API calls
"""


import logging
import requests

from user_profile import UserProfile
from constants import DELHIVERY_CREATE_PACKAGE_HEADERS
from response_handler import ResponseHandler


class DelhiveryBase(object):

    def __init__(self, user_profile):
        self.prepared_data = None
        self.url = None
        self.method = 'GET'
        self.headers = {}
        self.profile = UserProfile(**user_profile)
        self.logger = logging.getLogger(__name__)
        self.response = ResponseHandler({"success": False, "ok": False, "content": ''})

    def _prepare_pre_request_data(self, data):
        """
        This is abstract method and have to be over ridden in subclass.
        Inside subclass it will prepare the data for request.
        :return: None
        """
        pass

    def _prepare_response(self):
        """
        This is abstract method and have to be over ridden in subclass.
        This will prepare response accordingly.
        :return: None
        """
        pass

    def send_request(self, data):
        """
        Used to send the final SOAP request and to be called by subclass.
        It internally override the _send_request of subclass.
        :return: Response
        """
        try:
            self._prepare_pre_request_data(data)
            if self.method == 'GET':
                self.response = requests.get(self.url)
            else:
                self.response = requests.post(self.url, data=self.prepared_data, headers=self.headers, timeout=14)

        except Exception as exc:
            pass

        self._prepare_response()
        return self.response
