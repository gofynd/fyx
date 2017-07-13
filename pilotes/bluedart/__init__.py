import logging

from bluedart_exceptions import ParamValidationError
from zeep import Client
from zeep.exceptions import ValidationError, Fault
from response_handler import ResponseHandler


class BlueDart(object):
    def __init__(self, request_url, https=False):
        self.Profile = None
        self.response = {}
        self.logger = logging.getLogger(__name__)
        self.client = Client(request_url)
        self._prepare_pre_request_data()

    def _set_profile_credentials(self, user_profile):
        """
        Set profile credentials for the wsdl request.
        :param user_profile: Contains Profile object of creds.
        :return: WSDL profile param.
        """
        return self.Profile(
            Api_type=user_profile.api_type,
            LoginID=user_profile.login_id,
            LicenceKey=user_profile.license_key,
            Version=user_profile.version,
            Customercode=user_profile.customer_code
        )

    def _prepare_pre_request_data(self):

        """
        This should be treated as a abstract method and to be over ridden by each subclass.
        Prepare the wsdl request prefixes.
        :data - The incoming payload that will be converted into Bluedart's xml payload
        :return: None
        """
        pass

    def _send_request(self):
        """
        This is abstract method and have to be over ridden in subclass.
        Inside subclass it will decide which method to call for WSDL client.
        :return: None
        """
        pass

    def send_request(self):
        """
        Used to send the final SOAP request and to be called by subclass.
        It internally override the _send_request of subclass.
        :data - The incoming payload from the user
        :return: None
        """
        try:
            response = self._send_request()
            self.response = ResponseHandler(response)

        except Fault as fault:
            raise ParamValidationError(message=fault.message, code=fault.code)

        except Exception as exc:
            pass
        return self.response
