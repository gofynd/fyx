"""
File: services
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

It contains XML helper parser methods required to parse the response sent by delhivery.
"""
import xml.etree.cElementTree as ET


class DelhiveryXMLHelper(object):
    def __init__(self, xml_string):
        self.xml_string = xml_string
        self.status_dict = dict()

    def parse(self):
        if self.xml_string:
            root = ET.fromstring(self.xml_string)
            for child in root:
                self.status_dict[child.tag] = child.text
        return self.status_dict
