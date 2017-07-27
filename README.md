FyX
===
[![Build Status](https://travis-ci.org/gofynd/fyx.svg?branch=master)](https://travis-ci.org/gofynd/fyx)

<blockquote>
<p>
Fyx is an integration of multiple Delivery partners into a single project. It was created due to the problem faced by
us while integrating various DPS. All the DPS have different payloads and different content types for example Bluedart
uses XML, Delhivery uses JSON. So what is changed now with FYX you need not worry about the payload type and response
format, you will send and receive JSON.
</p>
</blockquote>


Current status, version 0.9.0, pre-alpha release
------------------------------------------------

This project is under development and at a very pre mature stage.

We are working to make it stable and make it ready for production.

THIS PROJECT IS UNDER DEVELOP MODE, IF YOU WANT TO USE IT -
FIX WHAT YOU NEED. FEEL FREE TO SEND US YOUR IMPROVISATIONS.

Right now we're targeting to integrate more delivery
partners to make your work easier.

Details
-------

Project codebase: <https://github.com/gofynd/fyx>

Project Documentation: <http://pilote.readthedocs.io/en/latest>


Delivery Partner integration is a very important step in building an ecommerce portal.
We realised the importance of the same and tried creating a layer which would involve less time and resource

FyX was build to solve the following issues:

- Indigenous Delivery Partner integration
- Lack of python based sdk's for most of the Delivery Partners
- Reduce the time taken for such integrations

Prior to FyX, Initially it would have taken something around 2 weeks for a single integration.
Now it can be done in less than a minute.




Currently we have integrated the following delivery partners:

- Blue Dart
- Delhivery
- Ecom Express

Delivery Partner API Docs
-------------------------
- Delhivery <https://goo.gl/4nsfsJ>
- Ecom Express <https://goo.gl/9yunXd>
- Blue Dart <https://goo.gl/CqS9Tz> 

Does it not sound cool enough..!!
Look how easy it is to use:


Features
--------

- One click installation
- All partners in one go
- Create Shipment
- Create Pickup
- Cancel Shipment
- Build things faster


To Come
-------

- Tracking Shipments
- More Delivery Partners
- Install Specific Delivery Partner
- Disable Delivery Partner
- Automated DP Assignments
- Logger
- Dynamic Status Mapping


Installation
------------

Install pilote by running:

    pip install pilote

Contribute
----------

- Issue Tracker: https://github.com/gofynd/fyx/issues
- Source Code: http://github.com/gofynd/fyx

Support
-------
At this point, we are expecting active contributions, feature suggestions
and raising  any/all kinds of issues.
If you are experiencing issues, please let us know.
You can raise the issue directly to github issue tracker.

About the Organisation
----------------------
Fynd is a product based Fashion Marketplace.
We at Fynd, believes a lot in open sourcing. As per our Open Sourcing policies, we are now making some essential modules Open Source so that anyone/everyone can benefit from the same.

License
-------

The project is licensed under the MIT License.


How to use
==========
```python

# Import the service you want to use.
# from pilotes.[pilote_name].services import CreateShipment, CancelShipment
from pilotes.ecomm.services import CreateShipment, CancelShipment

    def test_ecomm_create_package_success():

        TEST_CREDS = {
            "username": 'testusername',
            "password": 'testpass',
            "debug": True
        }

        # Test data set for sending request with params as key and param value as value.
        # Follow the documentation for dummy data.
        test_data = {}

        create_package = CreateShipment(TEST_CREDS, test_data)
        response = create_package.send_request()
        return response

```
