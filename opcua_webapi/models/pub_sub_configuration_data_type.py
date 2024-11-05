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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.pub_sub_connection_data_type import PubSubConnectionDataType
from opcua_webapi.models.published_data_set_data_type import PublishedDataSetDataType
from typing import Optional, Set
from typing_extensions import Self

class PubSubConfigurationDataType(BaseModel):
    """
    PubSubConfigurationDataType
    """ # noqa: E501
    published_data_sets: Optional[List[PublishedDataSetDataType]] = Field(default=None, alias="PublishedDataSets")
    connections: Optional[List[PubSubConnectionDataType]] = Field(default=None, alias="Connections")
    enabled: Optional[StrictBool] = Field(default=False, alias="Enabled")
    __properties: ClassVar[List[str]] = ["PublishedDataSets", "Connections", "Enabled"]

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
        """Create an instance of PubSubConfigurationDataType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in published_data_sets (list)
        _items = []
        if self.published_data_sets:
            for _item_published_data_sets in self.published_data_sets:
                if _item_published_data_sets:
                    _items.append(_item_published_data_sets.to_dict())
            _dict['PublishedDataSets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict['Connections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PubSubConfigurationDataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PublishedDataSets": [PublishedDataSetDataType.from_dict(_item) for _item in obj["PublishedDataSets"]] if obj.get("PublishedDataSets") is not None else None,
            "Connections": [PubSubConnectionDataType.from_dict(_item) for _item in obj["Connections"]] if obj.get("Connections") is not None else None,
            "Enabled": obj.get("Enabled") if obj.get("Enabled") is not None else False
        })
        return _obj


