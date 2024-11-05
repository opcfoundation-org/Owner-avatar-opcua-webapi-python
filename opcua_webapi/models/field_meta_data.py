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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from opcua_webapi.models.key_value_pair import KeyValuePair
from opcua_webapi.models.localized_text import LocalizedText
from typing import Optional, Set
from typing_extensions import Self

class FieldMetaData(BaseModel):
    """
    FieldMetaData
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    description: Optional[LocalizedText] = Field(default=None, alias="Description")
    field_flags: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=0, alias="FieldFlags")
    built_in_type: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=0, alias="BuiltInType")
    data_type: Optional[StrictStr] = Field(default=None, alias="DataType")
    value_rank: Optional[StrictInt] = Field(default=0, alias="ValueRank")
    array_dimensions: Optional[List[Annotated[int, Field(le=4294967295, strict=True, ge=0)]]] = Field(default=None, alias="ArrayDimensions")
    max_string_length: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=0, alias="MaxStringLength")
    data_set_field_id: Optional[StrictStr] = Field(default=None, alias="DataSetFieldId")
    properties: Optional[List[KeyValuePair]] = Field(default=None, alias="Properties")
    __properties: ClassVar[List[str]] = ["Name", "Description", "FieldFlags", "BuiltInType", "DataType", "ValueRank", "ArrayDimensions", "MaxStringLength", "DataSetFieldId", "Properties"]

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
        """Create an instance of FieldMetaData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['Description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item_properties in self.properties:
                if _item_properties:
                    _items.append(_item_properties.to_dict())
            _dict['Properties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FieldMetaData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Description": LocalizedText.from_dict(obj["Description"]) if obj.get("Description") is not None else None,
            "FieldFlags": obj.get("FieldFlags") if obj.get("FieldFlags") is not None else 0,
            "BuiltInType": obj.get("BuiltInType") if obj.get("BuiltInType") is not None else 0,
            "DataType": obj.get("DataType"),
            "ValueRank": obj.get("ValueRank") if obj.get("ValueRank") is not None else 0,
            "ArrayDimensions": obj.get("ArrayDimensions"),
            "MaxStringLength": obj.get("MaxStringLength") if obj.get("MaxStringLength") is not None else 0,
            "DataSetFieldId": obj.get("DataSetFieldId"),
            "Properties": [KeyValuePair.from_dict(_item) for _item in obj["Properties"]] if obj.get("Properties") is not None else None
        })
        return _obj


