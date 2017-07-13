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
DELHIVERY_FETCH_BULK_AWB = "/waybill/api/bulk/json/?cl={0}&action=fetch&count={1}&token={2}"
AWB_COUNT_FROM_CREATE_SHIPMENT = 1
TEST_CREDS = {
    'client_name': "XXXX - XXX",
    'api_token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'debug': True
}
DELHIVERY_DEBUG_BASE_URL = "http://test.delhivery.com"
DELHIVERY_BASE_URL = "https://track.delhivery.com"
DELHIVERY_DATA_FORMAT = "json"
SHIPMENT_TYPE = {"pre-paid": "pre-paid", "cod": "cod"}
