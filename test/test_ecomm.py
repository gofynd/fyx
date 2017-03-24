from random import randint

from pilotes.ecomm.services import CreateShipment, CancelShipment
from pilotes.ecomm.constants import TEST_CREDS

global_awb_number = None


def test_ecomm_create_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    order_number = 'FY' + str(randint(10001, 9999999))
    data = {"CONSIGNEE_ADDRESS2": "Police Station Ruksin", "CONSIGNEE_ADDRESS3": " ", "awb_type": "COD",
            "RETURN_MOBILE": "9899856639", "CONSIGNEE_ADDRESS1": "First House., Police Station Ruksin",
            "DESTINATION_CITY": "nadia", "PINCODE": "400072", "PICKUP_PINCODE": "400072", "PICKUP_MOBILE": "9899856639",
            "RETURN_PINCODE": "400072",
            "ORDER_NUMBER": order_number, "PICKUP_PHONE": "9899856639", "PICKUP_ADDRESS_LINE2": " ",
            "PICKUP_ADDRESS_LINE1": "Khasra No.201/09 12/19/22, Min 26 Revenue estate, Bhora Kalan",
            "COLLECTABLE_VALUE": 2049.0,
            "CONSIGNEE": "Tawram Taga", "DECLARED_VALUE": 2049.0, "VOLUMETRIC_WEIGHT": "0.499",
            "RETURN_ADDRESS_LINE1": "Khasra No.201/09 12/19/22, Min 26 Revenue estate, Bhora Kalan",
            "RETURN_ADDRESS_LINE2": " ", "RETURN_NAME": "Bhora Kalan",
            "ITEM_DESCRIPTION": "Blue and Black Running Shoes",
            "ACTUAL_WEIGHT": "0.499", "HEIGHT": "0.0", "STATE": "west bengal", "PIECES": "1",
            "PICKUP_NAME": "Bhora Kalan",
            "BREADTH": "0.0", "PRODUCT": "COD", "RETURN_PHONE": "9899856639", "MOBILE": "9954986463",
            "TELEPHONE": "9954986463", "LENGTH": "0.0"}
    response = create_package.send_request(data)
    global global_awb_number
    global_awb_number = response['shipments'][0]['awb']
    assert response['shipments'][0]['success'] == True


def test_ecomm_create_package_failure():
    """
    failure case for ecomm create package.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    response = create_package.send_request({})
    return response


def test_ecomm_cancel_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request({})
    return response


def test_ecomm_cancel_package_failure():
    """
    failure case for ecomm cancel package.
    :return:
    """
    data = {'waybill': global_awb_number}
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request(data)
    assert response['success'] == True
