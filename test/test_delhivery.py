from random import randint

from pilotes.delhivery.services import CreateShipment, CreatePickup, CancelShipment
from pilotes.delhivery.constants import TEST_CREDS

global_awb_number = None


def test_delhivery_create_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    order_number = 'FY' + str(randint(10001, 9999999))
    data = {"code": "Yepme01", "pin": 741102, "city": "nadia", "volumetric": 0.0, "weight": 499,
            "return_state": "haryana", "products_desc": "Blue and Black Running Shoes",
            "add": "First House., Police Station Ruksin",
            "state": "west bengal", "billable_weight": 499, "supplier": "Bhora Kalan",
            "dimensions": "0.00CM x 0.00CM x 0.00CM",
            "quantity": 1, "phone": "9954986463", "payment_mode": "cod", "order_date": "2017-03-02T10:21:23.001000",
            "name": "Tawram Taga",
            "return_add": "Khasra No.201/09 12/19/22, Min 26 Revenue estate, Bhora Kalan", "cod_amount": 2049.0,
            "total_amount": 2049.0,
            "seller_name": "Bhora Kalan", "return_city": "gurgaon", "country": "India",
            "seller_add": "Khasra No.201/09 12/19/22, Min 26 Revenue estate, Bhora Kalan",
            "return_pin": 122413, "retipurn_phone": "9899856639", "return_name": "Bhora Kalan", "order": order_number,
            "return_country": None}
    response = create_package.send_request(data)
    global global_awb_number
    global_awb_number = response['packages'][0]['waybill']
    assert response['success'] == True


def test_delhivery_create_package_failure():
    """
    failure case for delhivery create package.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    response = create_package.send_request({})
    return response


def test_delhivery_create_pickup_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return: response
    """
    create_pickup = CreatePickup(TEST_CREDS)
    response = create_pickup.send_request({})
    return response


def test_delhivery_create_pickup_failure():
    """
    failure case for delhivery create pickup.
    :return:
    """
    create_pickup = CreatePickup(TEST_CREDS)
    response = create_pickup.send_request({})
    return response


def test_delhivery_cancel_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    data = {'waybill': global_awb_number}
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request(data)
    assert response['error'] == 'Shipment status can not be changed as current status is UD Manifested'


def test_delhivery_cancel_package_failure():
    """
    failure case for delhivery cancel package.
    :return:
    """
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request({})
    return response
