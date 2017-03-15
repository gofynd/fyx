"""
File: response_handler
Author: Om Prakash <omprakash@gofynd.com>
Date: 17/02/2017

It handles the response in bluedart.
"""


class ResponseHandler(object):

    def __init__(self, response):
        self.status_code = 200
        self.response = response
        self.response_attributes = ['AWBNo', 'CCRCRDREF', 'DestinationArea', 'DestinationLocation', 'IsError',
                                    'ShipmentPickupDate', 'TokenNumber', "Status"]
        self.set_properties()

    def set_properties(self):
        for attr in self.response_attributes:
            if attr in self.response:
                self.response.__setattr__(attr, str(self.response[attr]))
            else:
                self.response.__setattr__(attr, '')
        return self

    def json(self):
        json_dict = {}
        for attr in self.response_attributes:
            json_dict[attr] = self.response[attr]

        return json_dict
