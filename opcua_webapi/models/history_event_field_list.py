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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.variant import Variant
from typing import Optional, Set
from typing_extensions import Self

class HistoryEventFieldList(BaseModel):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part11/6.6.4).
    """ # noqa: E501
    event_fields: Optional[List[Variant]] = Field(default=None, alias="EventFields")
    __properties: ClassVar[List[str]] = ["EventFields"]

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
        """Create an instance of HistoryEventFieldList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in event_fields (list)
        _items = []
        if self.event_fields:
            for _item_event_fields in self.event_fields:
                if _item_event_fields:
                    _items.append(_item_event_fields.to_dict())
            _dict['EventFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HistoryEventFieldList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "EventFields": [Variant.from_dict(_item) for _item in obj["EventFields"]] if obj.get("EventFields") is not None else None
        })
        return _obj


