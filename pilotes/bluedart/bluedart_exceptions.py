"""
File: bluedart_exceptions
Author: Om Prakash <omprakash@gofynd.com>
Date: 10/02/2017

It handles the exceptions in bluedart.
"""


class BluedartException(Exception):
    """
    Bluedart Exception class.
    """

    def __init__(self, code, msg):
        self.exc_code = code
        self.msg = msg

    def __unicode__(self):
        return "Error code: {}, Message: {}".format(self.exc_code, self.msg)

    def __str__(self):
        return self.__unicode__()


class ParamValidationError(BluedartException):
    """
    Exception: Missing params handling.
    """

    def __init__(self, code=-1, message=''):
        self.exc_code = code
        try:
            self.msg += 'Missing Parameters Exception: Details: {}'.format(message)
        except AttributeError:
            pass
