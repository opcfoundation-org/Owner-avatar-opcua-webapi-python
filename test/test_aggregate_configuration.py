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

from opcua_webapi.models.aggregate_configuration import AggregateConfiguration

class TestAggregateConfiguration(unittest.TestCase):
    """AggregateConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregateConfiguration:
        """Test AggregateConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregateConfiguration`
        """
        model = AggregateConfiguration()
        if include_optional:
            return AggregateConfiguration(
                use_server_capabilities_defaults = True,
                treat_uncertain_as_bad = True,
                percent_data_bad = 0,
                percent_data_good = 0,
                use_sloped_extrapolation = True
            )
        else:
            return AggregateConfiguration(
        )
        """

    def testAggregateConfiguration(self):
        """Test AggregateConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
