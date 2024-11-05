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

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from opcua_webapi.models.extension_object import ExtensionObject
from opcua_webapi.models.status_code import StatusCode
from typing import Optional, Set
from typing_extensions import Self

class HistoryReadResult(BaseModel):
    """
    HistoryReadResult
    """ # noqa: E501
    status_code: Optional[StatusCode] = Field(default=None, alias="StatusCode")
    continuation_point: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, alias="ContinuationPoint")
    history_data: Optional[ExtensionObject] = Field(default=None, alias="HistoryData")
    __properties: ClassVar[List[str]] = ["StatusCode", "ContinuationPoint", "HistoryData"]

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
        """Create an instance of HistoryReadResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status_code
        if self.status_code:
            _dict['StatusCode'] = self.status_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of history_data
        if self.history_data:
            _dict['HistoryData'] = self.history_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HistoryReadResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "StatusCode": StatusCode.from_dict(obj["StatusCode"]) if obj.get("StatusCode") is not None else None,
            "ContinuationPoint": obj.get("ContinuationPoint"),
            "HistoryData": ExtensionObject.from_dict(obj["HistoryData"]) if obj.get("HistoryData") is not None else None
        })
        return _obj


