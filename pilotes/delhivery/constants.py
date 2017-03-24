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
    'client_name': "FYND - NDD",
    'api_token': '174780ea32804e33bbc80f6aef5bf0d19b79ca25',
    'debug': True
}
DELHIVERY_DEBUG_BASE_URL = "http://test.delhivery.com"
DELHIVERY_BASE_URL = "https://track.delhivery.com"
DELHIVERY_DATA_FORMAT = "json"
