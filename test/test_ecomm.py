from random import randint

from pilotes.ecomm.services import CreateShipment, CancelShipment
from pilotes.ecomm.constants import TEST_CREDS

global_awb_number = None


def test_ecomm_create_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    order_number = 'FY' + str(randint(10001, 9999999))
    data = {"consignee_address2": "65,Shakti Nagar,Near Bhole Kuti,Gupteshwar", "breadth": "0.00",
            "consignee_address1": "C/o B.D.Mishra", "rto_name": "Nelamangala Taluk", "weight": "490.0",
            "quantity": 1, "consignee_state": "madhya pradesh", "rto_pincode": "562123", "consignee_pincode": "400072",
            "rto_state": "Maharashtra", "height": "0.00", "rto_country": "india", "pickup_mobile": "8147786893",
            "pickup_pincode": "562123", "order_date": "2017-04-06T16:09:10.001000", "consignee_country": "India",
            "pickup_name": "Nelamangala Taluk", "shipment_number": order_number, "volumetric": "0.0",
            "return_name": "Fynd/Shopsense Retail Technologies", "product_cod_value": 374.0, "rto_phone": "8147786893",
            "awb_num": "", "pickup_address1": "C/o Innovative Logistics, Survey No 72/5",
            "pickup_address2": "Vajrahalli Village, Bhaktanpalya Road, Nelamangala", "consignee_phone": "9407267140",
            "rto_address2": "Vajrahalli Village, Bhaktanpalya Road, Nelamangala", "consignee_mobile": "9407267140",
            "pickup_phone": "8147786893", "shipment_type": "pre-paid",
            "rto_address1": "C/o Innovative Logistics, Survey No 72/5", "length": "0.00", "warehouse_code": "FYND501",
            "rto_mobile": "8147786893", "rto_city": "mumbai", "consignee_city": "jabalpur",
            "product_name": "Black Slip-ons", "consignee_name": "Shikha Tripathi"}
    create_package = CreateShipment(TEST_CREDS, data)
    response = create_package.send_request()
    global global_awb_number

    global_awb_number = response['shipments'][0]['awb']
    assert response['shipments'][0]['success'] == True


def test_ecomm_create_package_failure():
    """
    failure case for ecomm create package.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS, {})
    response = create_package.send_request()
    return response


def test_ecomm_cancel_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    cancel_package = CancelShipment(TEST_CREDS, {})
    response = cancel_package.send_request()
    return response


def test_ecomm_cancel_package_failure():
    """
    failure case for ecomm cancel package.
    :return:
    """
    data = {'waybill': global_awb_number}
    cancel_package = CancelShipment(TEST_CREDS, data)
    response = cancel_package.send_request()
    assert response['success'] == True
