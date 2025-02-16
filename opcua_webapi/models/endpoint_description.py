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

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from opcua_webapi.models.application_description import ApplicationDescription
from opcua_webapi.models.user_token_policy import UserTokenPolicy
from typing import Optional, Set
from typing_extensions import Self

class EndpointDescription(BaseModel):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.14).
    """ # noqa: E501
    endpoint_url: Optional[StrictStr] = Field(default=None, alias="EndpointUrl")
    server: Optional[ApplicationDescription] = Field(default=None, alias="Server")
    server_certificate: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, alias="ServerCertificate")
    security_mode: Optional[StrictInt] = Field(default=None, description="[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.3.10).", alias="SecurityMode")
    security_policy_uri: Optional[StrictStr] = Field(default=None, alias="SecurityPolicyUri")
    user_identity_tokens: Optional[List[UserTokenPolicy]] = Field(default=None, alias="UserIdentityTokens")
    transport_profile_uri: Optional[StrictStr] = Field(default=None, alias="TransportProfileUri")
    security_level: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=0, alias="SecurityLevel")
    __properties: ClassVar[List[str]] = ["EndpointUrl", "Server", "ServerCertificate", "SecurityMode", "SecurityPolicyUri", "UserIdentityTokens", "TransportProfileUri", "SecurityLevel"]

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
        """Create an instance of EndpointDescription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['Server'] = self.server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in user_identity_tokens (list)
        _items = []
        if self.user_identity_tokens:
            for _item_user_identity_tokens in self.user_identity_tokens:
                if _item_user_identity_tokens:
                    _items.append(_item_user_identity_tokens.to_dict())
            _dict['UserIdentityTokens'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointDescription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "EndpointUrl": obj.get("EndpointUrl"),
            "Server": ApplicationDescription.from_dict(obj["Server"]) if obj.get("Server") is not None else None,
            "ServerCertificate": obj.get("ServerCertificate"),
            "SecurityMode": obj.get("SecurityMode"),
            "SecurityPolicyUri": obj.get("SecurityPolicyUri"),
            "UserIdentityTokens": [UserTokenPolicy.from_dict(_item) for _item in obj["UserIdentityTokens"]] if obj.get("UserIdentityTokens") is not None else None,
            "TransportProfileUri": obj.get("TransportProfileUri"),
            "SecurityLevel": obj.get("SecurityLevel") if obj.get("SecurityLevel") is not None else 0
        })
        return _obj


