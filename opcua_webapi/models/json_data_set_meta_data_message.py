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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from opcua_webapi.models.data_set_meta_data_type import DataSetMetaDataType
from typing import Optional, Set
from typing_extensions import Self

class JsonDataSetMetaDataMessage(BaseModel):
    """
    [Link to specification]().
    """ # noqa: E501
    message_id: Optional[StrictStr] = Field(default=None, alias="MessageId")
    message_type: Optional[StrictStr] = Field(default=None, alias="MessageType")
    publisher_id: Optional[StrictStr] = Field(default=None, alias="PublisherId")
    data_set_writer_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=0, alias="DataSetWriterId")
    writer_group_name: Optional[StrictStr] = Field(default=None, alias="WriterGroupName")
    data_set_writer_name: Optional[StrictStr] = Field(default=None, alias="DataSetWriterName")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    meta_data: Optional[DataSetMetaDataType] = Field(default=None, alias="MetaData")
    __properties: ClassVar[List[str]] = ["MessageId", "MessageType", "PublisherId", "DataSetWriterId", "WriterGroupName", "DataSetWriterName", "Timestamp", "MetaData"]

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
        """Create an instance of JsonDataSetMetaDataMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta_data
        if self.meta_data:
            _dict['MetaData'] = self.meta_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonDataSetMetaDataMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MessageId": obj.get("MessageId"),
            "MessageType": obj.get("MessageType"),
            "PublisherId": obj.get("PublisherId"),
            "DataSetWriterId": obj.get("DataSetWriterId") if obj.get("DataSetWriterId") is not None else 0,
            "WriterGroupName": obj.get("WriterGroupName"),
            "DataSetWriterName": obj.get("DataSetWriterName"),
            "Timestamp": obj.get("Timestamp"),
            "MetaData": DataSetMetaDataType.from_dict(obj["MetaData"]) if obj.get("MetaData") is not None else None
        })
        return _obj


