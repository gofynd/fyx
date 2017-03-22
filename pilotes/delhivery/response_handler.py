"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
.. note::
    This file parses the response for all Delhivery API call.

"""


class ResponseHandler(object):
    """This is a helper class which creates valid response for all
    Delhivery API calls
    """

    def __init__(self, response):
        """Initialization method for ResponseHandler base class, which sets
        raw response that will be processed here

        Args:
            response - This will be raw response generated
        """

        self.status_code = 200
        self.response = response
        self.response_attributes = response.keys()
        self.set_properties()

    def set_properties(self):
        """It sets the properties for the response
        Args:
            None
        :return:
            Formatted JSON equivalent
        """

        for attr in self.response_attributes:
            if attr in self.response:
                self.__setattr__(attr, self.response[attr])
        return self

    def json(self):
        """It converts response to JSON
        Args:
            None
        :return:
            JSON response
        """

        json_dict = {}
        for attr in self.response_attributes:
            json_dict[attr] = self.response[attr]

        return json_dict
