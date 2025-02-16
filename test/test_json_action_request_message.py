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

from opcua_webapi.models.json_action_request_message import JsonActionRequestMessage

class TestJsonActionRequestMessage(unittest.TestCase):
    """JsonActionRequestMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonActionRequestMessage:
        """Test JsonActionRequestMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonActionRequestMessage`
        """
        model = JsonActionRequestMessage()
        if include_optional:
            return JsonActionRequestMessage(
                data_set_writer_id = 0,
                action_target_id = 0,
                data_set_writer_name = '',
                writer_group_name = '',
                meta_data_version = opcua_webapi.models.configuration_version_data_type.ConfigurationVersionDataType(
                    major_version = 0, 
                    minor_version = 0, ),
                minor_version = 0,
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                message_type = '',
                request_id = 0,
                action_state = 56,
                payload = None
            )
        else:
            return JsonActionRequestMessage(
        )
        """

    def testJsonActionRequestMessage(self):
        """Test JsonActionRequestMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
