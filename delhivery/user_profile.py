"""
File: user_profile
Author: Vineet Dubey <vineetdubey@gofynd.com>
Date: 10/02/2017

This is the user credentials  for Ecomm profile.
"""


class UserProfile(object):
    """
    Set the user credentials for API requests.
    """
    def __init__(self, client_name, api_token, debug=False):
        self.client_name = client_name
        self.api_token = api_token
        self.debug = debug
