import datetime

from pilotes.bluedart.services import CreateShipment, CancelShipment, CreatePickup
from pilotes.bluedart.constants import TEST_CREDS
import random


def test_bluedart_create_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    # TODO: Pickup date logic to be calculated.
    pickup_date = datetime.datetime.now().date()
    threshold_date = (datetime.datetime.now() + datetime.timedelta(hours=11)).date()
    if pickup_date != threshold_date:
        pickup_date = threshold_date

    create_package.consignee = create_package.Consignee(
        ConsigneeName='Om Prakash',
        ConsigneeMobile='8452858570',
        ConsigneeAddress1='Kaustubham Apartment',
        ConsigneeAddress2='Gokuldham',
        ConsigneeAddress3='Mumbai',
        ConsigneePincode='400063',
        ConsigneeTelephone=""
    )

    create_package.shipper = create_package.Shipper(
        CustomerName='FYND',
        CustomerAddress1='Corporate Center',
        CustomerAddress2='5th Floor',
        CustomerAddress3='Mumbai',
        CustomerCode='099960',
        OriginArea='BOM',
        Sender='Fynd',
        CustomerPincode='400072',
        CustomerMobile='8452858570',
        CustomerTelephone="",
    )

    commodity = create_package.Commodity (
        CommodityDetail1='Jeans',
        CommodityDetail2='Pepejeans',
        CommodityDetail3='Blue'
    )

    # Shipping Item Details
    dimensions = create_package.dimension(
        Breadth=10,
        Height=10,
        Length=10,
        Count=1
    )
    create_package.services = create_package.Services(
        ActualWeight=0.5,
        CollectableAmount=1500,
        CreditReferenceNo="FY" + str(random.randrange(111111, 999999, 6)),
        DeclaredValue=1500,
        InvoiceNo='839903890',
        PickupTime='1800',
        PieceCount=1,
        ProductCode='A',
        ProductType='Dutiables',
        SubProductCode="C",
        Commodity=commodity,
        Dimensions=[dimensions],
        PickupDate=pickup_date,
        RegisterPickup=True
    )
    response = create_package.send_request()
    return response


def test_bluedart_create_package_failure():
    """
    failure case for bluedart create package.
    :return:
    """
    create_package = CreateShipment(TEST_CREDS)
    response = create_package.send_request()
    return response


def test_bluedart_cancel_package_success():
    """
    TODO: Success case to be written with a dummy set of valid data.
    :return:
    """
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request()
    return response


def test_bluedart_cancel_package_failure():
    """
    failure case for bluedart cancel package.
    :return:
    """
    cancel_package = CancelShipment(TEST_CREDS)
    response = cancel_package.send_request()
    return response
