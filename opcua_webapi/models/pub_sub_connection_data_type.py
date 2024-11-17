# coding: utf-8

"""
    OPC UA Web API

    Provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.key_value_pair import KeyValuePair
from opcua_webapi.models.reader_group_data_type import ReaderGroupDataType
from opcua_webapi.models.variant import Variant
from opcua_webapi.models.writer_group_data_type import WriterGroupDataType
from typing import Optional, Set
from typing_extensions import Self

class PubSubConnectionDataType(BaseModel):
    """
    PubSubConnectionDataType
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    enabled: Optional[StrictBool] = Field(default=False, alias="Enabled")
    publisher_id: Optional[Variant] = Field(default=None, alias="PublisherId")
    transport_profile_uri: Optional[StrictStr] = Field(default=None, alias="TransportProfileUri")
    address: Optional[Dict[str, Any]] = Field(default=None, alias="Address")
    connection_properties: Optional[List[KeyValuePair]] = Field(default=None, alias="ConnectionProperties")
    transport_settings: Optional[Dict[str, Any]] = Field(default=None, alias="TransportSettings")
    writer_groups: Optional[List[WriterGroupDataType]] = Field(default=None, alias="WriterGroups")
    reader_groups: Optional[List[ReaderGroupDataType]] = Field(default=None, alias="ReaderGroups")
    __properties: ClassVar[List[str]] = ["Name", "Enabled", "PublisherId", "TransportProfileUri", "Address", "ConnectionProperties", "TransportSettings", "WriterGroups", "ReaderGroups"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PubSubConnectionDataType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of publisher_id
        if self.publisher_id:
            _dict['PublisherId'] = self.publisher_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in connection_properties (list)
        _items = []
        if self.connection_properties:
            for _item_connection_properties in self.connection_properties:
                if _item_connection_properties:
                    _items.append(_item_connection_properties.to_dict())
            _dict['ConnectionProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in writer_groups (list)
        _items = []
        if self.writer_groups:
            for _item_writer_groups in self.writer_groups:
                if _item_writer_groups:
                    _items.append(_item_writer_groups.to_dict())
            _dict['WriterGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reader_groups (list)
        _items = []
        if self.reader_groups:
            for _item_reader_groups in self.reader_groups:
                if _item_reader_groups:
                    _items.append(_item_reader_groups.to_dict())
            _dict['ReaderGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PubSubConnectionDataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Enabled": obj.get("Enabled") if obj.get("Enabled") is not None else False,
            "PublisherId": Variant.from_dict(obj["PublisherId"]) if obj.get("PublisherId") is not None else None,
            "TransportProfileUri": obj.get("TransportProfileUri"),
            "Address": obj.get("Address"),
            "ConnectionProperties": [KeyValuePair.from_dict(_item) for _item in obj["ConnectionProperties"]] if obj.get("ConnectionProperties") is not None else None,
            "TransportSettings": obj.get("TransportSettings"),
            "WriterGroups": [WriterGroupDataType.from_dict(_item) for _item in obj["WriterGroups"]] if obj.get("WriterGroups") is not None else None,
            "ReaderGroups": [ReaderGroupDataType.from_dict(_item) for _item in obj["ReaderGroups"]] if obj.get("ReaderGroups") is not None else None
        })
        return _obj


