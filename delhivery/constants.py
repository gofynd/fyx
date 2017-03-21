"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
.. note::
   All constants required for Delhivery API are placed here.

"""


DELHIVERY_CREATE_PACKAGE = "/cmu/push/json/?token={}"  # .format(DELHIVERY_API_TOKEN)
DELHIVERY_CREATE_PACKAGE_HEADERS = {"content-type": "application/x-www-form-urlencoded"}
DELHIVERY_CREATE_PICKUP_HEADERS = {'Content-Type': 'application/json',
                                   'Authorization': 'Token {}'}  # .format(DELHIVERY_API_TOKEN)}
DELHIVERY_CANCEL_PACKAGE_HEADERS = DELHIVERY_CREATE_PICKUP_HEADERS
DELHIVERY_CANCEL_PACKAGE = "/api/p/edit"
DELHIVERY_CREATE_PICKUP = "/fm/request/new/"
TEST_CREDS = {
    'client_name': "XXX - TEST",
    'api_token': '98723ksdjwiou923709xns980932nsdfie0'
}
DELHIVERY_DEBUG_BASE_URL = "http://test.delhivery.com"
DELHIVERY_BASE_URL = "https://track.delhivery.com"
