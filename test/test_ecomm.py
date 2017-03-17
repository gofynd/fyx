from ecomm.services import CreatePackage, CancelShipment
from ecomm.constants import TEST_CREDS


def test_ecomm_create_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    create_package = CreatePackage(TEST_CREDS)
    response = create_package.send_request({})
    return response


def test_ecomm_create_package_failure():
    """
    failure case for ecomm create package.
    :return:
    """
    create_package = CreatePackage(TEST_CREDS)
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
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request({})
    return response
