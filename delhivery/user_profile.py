"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 10/02/2017
File: user_profile
This file sets the user credentials  for Delhivery profile.
"""


class UserProfile(object):
    """
    Set the user credentials for API requests.
    """
    def __init__(self, client_name, api_token, debug=False):
        """Initialization method for UserProfile class, which sets
        credentials for using Delhivery API

        Args:
            client_name - Client name for delhivery.
            api_token - Token for using the delhivery API
        """
        self.client_name = client_name
        self.api_token = api_token
        self.debug = debug
