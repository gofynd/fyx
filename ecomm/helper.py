"""
File: services
Author: Vineet Kumar Dubey <vineetdubey@gofynd.com>
Date: 04/03/2017

It contains XML helper parser methods required to parse the response sent by delhivery.
"""
import xml.etree.cElementTree as ET


class ECOMXMLParser(object):
    def __init__(self, xml_string):
        self.xml_string = xml_string
        self.awb_dict = dict()
        self.awb_dict['status_list'] = []
        self.status_dict = dict()

    def parse_reverse_shipment_response(self):
        root = ET.fromstring(self.xml_string)
        root_object = root.find('AIRWAYBILL-OBJECTS')
        for object_child in root_object:
            if object_child.tag == "AIRWAYBILL":
                for child in object_child:
                    self.status_dict[child.tag] = child.text
        return self.status_dict
