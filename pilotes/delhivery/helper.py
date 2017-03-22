"""
.. module:: Delhivery
.. moduleauthor:: Vineet Kumar Dubey <vineetdubey@gofynd.com>
.. note::
    It contains XML helper parser methods required to parse the response sent by delhivery.
"""
import xml.etree.cElementTree as ET


class DelhiveryXMLHelper(object):
    """This is a helper class which parses the xml response send
    by the delhivery to JSON
    """

    def __init__(self, xml_string):
        """Initialization method for DelhiveryXMLHelper class, which
        initializes the xml_string
        """

        self.xml_string = xml_string
        self.status_dict = dict()

    def parse(self):
        """This method simply parses the initialized xml_string to
        JSON Response
        Args:
            None
        :return: JSON equivalent of the xml_string
        """

        if self.xml_string:
            root = ET.fromstring(self.xml_string)
            for child in root:
                self.status_dict[child.tag] = child.text
        return self.status_dict
