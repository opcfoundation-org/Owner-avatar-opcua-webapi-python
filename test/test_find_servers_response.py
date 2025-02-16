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

from opcua_webapi.models.find_servers_response import FindServersResponse

class TestFindServersResponse(unittest.TestCase):
    """FindServersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindServersResponse:
        """Test FindServersResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindServersResponse`
        """
        model = FindServersResponse()
        if include_optional:
            return FindServersResponse(
                response_header = opcua_webapi.models.response_header.ResponseHeader(
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    request_handle = 0, 
                    service_result = opcua_webapi.models.status_code.StatusCode(
                        code = 0, 
                        symbol = '', ), 
                    service_diagnostics = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
                        symbolic_id = 56, 
                        namespace_uri = 56, 
                        locale = 56, 
                        localized_text = 56, 
                        additional_info = '', 
                        inner_status_code = opcua_webapi.models.status_code.StatusCode(
                            code = 0, 
                            symbol = '', ), 
                        inner_diagnostic_info = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
                            symbolic_id = 56, 
                            namespace_uri = 56, 
                            locale = 56, 
                            localized_text = 56, 
                            additional_info = '', ), ), 
                    string_table = [
                        ''
                        ], 
                    additional_header = opcua_webapi.models.extension_object.ExtensionObject(
                        ua_type_id = '', 
                        ua_encoding = 0, 
                        ua_body = 'YQ==', ), ),
                servers = [
                    opcua_webapi.models.application_description.ApplicationDescription(
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
                            ], )
                    ]
            )
        else:
            return FindServersResponse(
        )
        """

    def testFindServersResponse(self):
        """Test FindServersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
