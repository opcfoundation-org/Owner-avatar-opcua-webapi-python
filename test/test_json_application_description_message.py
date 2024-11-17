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

from opcua_webapi.models.json_application_description_message import JsonApplicationDescriptionMessage

class TestJsonApplicationDescriptionMessage(unittest.TestCase):
    """JsonApplicationDescriptionMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonApplicationDescriptionMessage:
        """Test JsonApplicationDescriptionMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonApplicationDescriptionMessage`
        """
        model = JsonApplicationDescriptionMessage()
        if include_optional:
            return JsonApplicationDescriptionMessage(
                message_id = '',
                message_type = '',
                publisher_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = opcua_webapi.models.application_description.ApplicationDescription(
                    application_uri = '', 
                    product_uri = '', 
                    application_name = opcua_webapi.models.localized_text.LocalizedText(
                        locale = '', 
                        text = '', ), 
                    application_type = 56, 
                    gateway_server_uri = '', 
                    discovery_profile_uri = '', 
                    discovery_urls = [
                        ''
                        ], ),
                server_capabilities = [
                    ''
                    ]
            )
        else:
            return JsonApplicationDescriptionMessage(
        )
        """

    def testJsonApplicationDescriptionMessage(self):
        """Test JsonApplicationDescriptionMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
