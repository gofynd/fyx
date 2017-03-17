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
    def __init__(self, username, password, debug=False):
        self.username = username
        self.password = password
        self.debug = debug
