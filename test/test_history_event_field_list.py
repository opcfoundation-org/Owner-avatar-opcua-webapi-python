# coding: utf-8

"""
    OPC UA Web API

    Provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opcua_webapi.models.history_event_field_list import HistoryEventFieldList

class TestHistoryEventFieldList(unittest.TestCase):
    """HistoryEventFieldList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HistoryEventFieldList:
        """Test HistoryEventFieldList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HistoryEventFieldList`
        """
        model = HistoryEventFieldList()
        if include_optional:
            return HistoryEventFieldList(
                event_fields = [
                    opcua_webapi.models.variant.Variant(
                        ua_type = 0, 
                        value = null, 
                        dimensions = [
                            0
                            ], )
                    ]
            )
        else:
            return HistoryEventFieldList(
        )
        """

    def testHistoryEventFieldList(self):
        """Test HistoryEventFieldList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
