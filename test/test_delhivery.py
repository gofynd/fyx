from pilotes.delhivery.services import CreateShipment, CreatePickup, CancelShipment
from pilotes.delhivery.constants import TEST_CREDS


def test_delhivery_create_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    response = create_package.send_request({})
    return response


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
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request({})
    return response


def test_delhivery_cancel_package_failure():
    """
    failure case for delhivery cancel package.
    :return:
    """
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request({})
    return response
