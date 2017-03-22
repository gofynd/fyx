======
Pilote
======

.. image:: https://api.travis-ci.org/omprakash1989/pilote.svg?branch=master
   :alt: build status
   :target: https://travis-ci.org/omprakash1989/pilote

THIS PROJECT IS UNDER DEVELOP MODE, IF YOU WANT TO USE IT - FIX WHAT YOU NEED. FEEL FREE TO SEND US YOUR IMPROVISATIONS.

Right now we're targeting to integrate more delivery partners to make your work easier.


Details
-------

Project codebase: <https://github.com/omprakash1989/pilote>

Project Documentation: <http://pilote.readthedocs.io/en/latest>


Working
-------

* [ok] Create New Shipments.
* [ok] Cancel Shipments
* [ok] Create pickups
* [WIP] Auth
* [WIP] Customization according to requirements
* [WIP] Polling Shipment Status

Current status, version 0.7.0, pre-alpha release
------------------------------------------------

This project is under development and at a very pre mature stage.

We are working to make it stable and make it ready for production.


Current Pilotes available
-------------------------

Bluedart

Delhivery

Ecomm


TODO
----

* Improvisation in documentation.
* Integrity in response.
* Add more pilotes.
* Developer customization in installation.
* Post shipment status polling.


Installations
=============

``pip install pilote``

Usage
=====
``# Import the service you want to use.``

``# from pilotes.[pilote_name].services import CreateShipment, CancelShipment, CreatePickup``
.. code::
    from pilotes.ecomm.services import CreateShipment, CancelShipment, CreatePickup

        def test_ecomm_create_package_success():

            TEST_CREDS = TEST_CREDS = {
                "username": 'testusername',
                "password": 'testpass',
                "debug": True
            }

            # Test data set for sending request with params as key and param value as value.
            # Follow the documentation for dummy data.
            test_data = {}

            create_package = CreateShipment(TEST_CREDS)
            response = create_package.send_request(test_data)
            return response
