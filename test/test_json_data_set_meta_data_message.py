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

from opcua_webapi.models.json_data_set_meta_data_message import JsonDataSetMetaDataMessage

class TestJsonDataSetMetaDataMessage(unittest.TestCase):
    """JsonDataSetMetaDataMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonDataSetMetaDataMessage:
        """Test JsonDataSetMetaDataMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonDataSetMetaDataMessage`
        """
        model = JsonDataSetMetaDataMessage()
        if include_optional:
            return JsonDataSetMetaDataMessage(
                message_id = '',
                message_type = '',
                publisher_id = '',
                data_set_writer_id = 0,
                writer_group_name = '',
                data_set_writer_name = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                meta_data = opcua_webapi.models.data_set_meta_data_type.DataSetMetaDataType(
                    name = '', 
                    description = opcua_webapi.models.localized_text.LocalizedText(
                        locale = '', 
                        text = '', ), 
                    fields = [
                        opcua_webapi.models.field_meta_data.FieldMetaData(
                            name = '', 
                            field_flags = 0, 
                            built_in_type = 0, 
                            data_type = '', 
                            value_rank = 56, 
                            array_dimensions = [
                                0
                                ], 
                            max_string_length = 0, 
                            data_set_field_id = '', 
                            properties = [
                                opcua_webapi.models.key_value_pair.KeyValuePair(
                                    key = '', 
                                    value = opcua_webapi.models.variant.Variant(
                                        ua_type = 0, 
                                        body = null, 
                                        dimensions = [
                                            0
                                            ], ), )
                                ], )
                        ], 
                    data_set_class_id = '', 
                    configuration_version = opcua_webapi.models.configuration_version_data_type.ConfigurationVersionDataType(
                        major_version = 0, 
                        minor_version = 0, ), )
            )
        else:
            return JsonDataSetMetaDataMessage(
        )
        """

    def testJsonDataSetMetaDataMessage(self):
        """Test JsonDataSetMetaDataMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
