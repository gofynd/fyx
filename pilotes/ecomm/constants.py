"""
File: constants
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

This file contains the constants needed for making Ecomm API calls
"""

ECOM_PLACE_SHIPMENT = "/apiv2/manifest_awb/"
ECOM_CANCEL_SHIPMENT = "/apiv2/cancel_awb/"
ECOM_DEBUG_BASE_URL = "http://ecomm.prtouch.com"
ECOM_BASE_URL = "http://api.ecomexpress.in"
ECOM_FETCH_AWBS = "/apiv2/fetch_awb/"
AWB_COUNT_FROM_CREATE_SHIPMENT = 1
TEST_CREDS = {
    "username": 'ecomexpress',
    "password": 'Ke$3c@4oT5m6h#$',
    "debug": True
}
SHIPMENT_TYPE = {"pre-paid": "PPD", "cod": "COD"}
