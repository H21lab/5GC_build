# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.api_ie_mapping import ApiIeMapping
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.ie_type import IeType
from openapi_server import util

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.api_ie_mapping import ApiIeMapping  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.ie_type import IeType  # noqa: E501

class ProtectionPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, api_ie_mapping_list=None, data_type_enc_policy=None):  # noqa: E501
        """ProtectionPolicy - a model defined in OpenAPI

        :param api_ie_mapping_list: The api_ie_mapping_list of this ProtectionPolicy.  # noqa: E501
        :type api_ie_mapping_list: List[ApiIeMapping]
        :param data_type_enc_policy: The data_type_enc_policy of this ProtectionPolicy.  # noqa: E501
        :type data_type_enc_policy: List[IeType]
        """
        self.openapi_types = {
            'api_ie_mapping_list': List[ApiIeMapping],
            'data_type_enc_policy': List[IeType]
        }

        self.attribute_map = {
            'api_ie_mapping_list': 'apiIeMappingList',
            'data_type_enc_policy': 'dataTypeEncPolicy'
        }

        self._api_ie_mapping_list = api_ie_mapping_list
        self._data_type_enc_policy = data_type_enc_policy

    @classmethod
    def from_dict(cls, dikt) -> 'ProtectionPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProtectionPolicy of this ProtectionPolicy.  # noqa: E501
        :rtype: ProtectionPolicy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_ie_mapping_list(self):
        """Gets the api_ie_mapping_list of this ProtectionPolicy.


        :return: The api_ie_mapping_list of this ProtectionPolicy.
        :rtype: List[ApiIeMapping]
        """
        return self._api_ie_mapping_list

    @api_ie_mapping_list.setter
    def api_ie_mapping_list(self, api_ie_mapping_list):
        """Sets the api_ie_mapping_list of this ProtectionPolicy.


        :param api_ie_mapping_list: The api_ie_mapping_list of this ProtectionPolicy.
        :type api_ie_mapping_list: List[ApiIeMapping]
        """
        if api_ie_mapping_list is None:
            raise ValueError("Invalid value for `api_ie_mapping_list`, must not be `None`")  # noqa: E501

        self._api_ie_mapping_list = api_ie_mapping_list

    @property
    def data_type_enc_policy(self):
        """Gets the data_type_enc_policy of this ProtectionPolicy.


        :return: The data_type_enc_policy of this ProtectionPolicy.
        :rtype: List[IeType]
        """
        return self._data_type_enc_policy

    @data_type_enc_policy.setter
    def data_type_enc_policy(self, data_type_enc_policy):
        """Sets the data_type_enc_policy of this ProtectionPolicy.


        :param data_type_enc_policy: The data_type_enc_policy of this ProtectionPolicy.
        :type data_type_enc_policy: List[IeType]
        """

        self._data_type_enc_policy = data_type_enc_policy
