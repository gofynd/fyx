"""
File: user_profile
Author: Om Prakash <omprakash@gofynd.com>
Date: 10/02/2017

This is the user creds for bluedart profile.
"""


class UserProfile(object):
    """
    Set the user credentials for API requests.
    """
    def __init__(self, api_type, login_id, licence_key, area=None, customer_code=None, is_admin=None, password=None,
                 version=None, tracking_license_key=None, debug=False):
        self.api_type = api_type
        self.login_id = login_id
        self.password = password
        self.area = area
        self.customer_code = customer_code
        self.is_admin = is_admin
        self.license_key = licence_key
        self.version = version
        self.tracking_license_key = tracking_license_key
        self.debug = debug
