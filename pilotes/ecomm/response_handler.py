"""
File: response_handler
Author: Om Prakash <omprakash@gofynd.com>
Date: 17/02/2017

It handles the response in ecomm.
"""


class ResponseHandler(object):

    def __init__(self, response):
        self.status_code = 200
        self.response = response
        self.response_attributes = response.keys()
        self.set_properties()

    def set_properties(self):
        for attr in self.response_attributes:
            if attr in self.response:
                self.__setattr__(attr, self.response[attr])
        return self

    def json(self):
        json_dict = {}
        for attr in self.response_attributes:
            json_dict[attr] = self.response[attr]

        return json_dict
