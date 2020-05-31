# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.api_signature import ApiSignature
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.http_method import HttpMethod
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.ie_info import IeInfo
from openapi_server import util

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.api_signature import ApiSignature  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.http_method import HttpMethod  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.ie_info import IeInfo  # noqa: E501

class ApiIeMapping(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, api_signature=None, api_method=None, ie_list=None):  # noqa: E501
        """ApiIeMapping - a model defined in OpenAPI

        :param api_signature: The api_signature of this ApiIeMapping.  # noqa: E501
        :type api_signature: ApiSignature
        :param api_method: The api_method of this ApiIeMapping.  # noqa: E501
        :type api_method: HttpMethod
        :param ie_list: The ie_list of this ApiIeMapping.  # noqa: E501
        :type ie_list: List[IeInfo]
        """
        self.openapi_types = {
            'api_signature': ApiSignature,
            'api_method': HttpMethod,
            'ie_list': List[IeInfo]
        }

        self.attribute_map = {
            'api_signature': 'apiSignature',
            'api_method': 'apiMethod',
            'ie_list': 'IeList'
        }

        self._api_signature = api_signature
        self._api_method = api_method
        self._ie_list = ie_list

    @classmethod
    def from_dict(cls, dikt) -> 'ApiIeMapping':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApiIeMapping of this ApiIeMapping.  # noqa: E501
        :rtype: ApiIeMapping
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_signature(self):
        """Gets the api_signature of this ApiIeMapping.


        :return: The api_signature of this ApiIeMapping.
        :rtype: ApiSignature
        """
        return self._api_signature

    @api_signature.setter
    def api_signature(self, api_signature):
        """Sets the api_signature of this ApiIeMapping.


        :param api_signature: The api_signature of this ApiIeMapping.
        :type api_signature: ApiSignature
        """
        if api_signature is None:
            raise ValueError("Invalid value for `api_signature`, must not be `None`")  # noqa: E501

        self._api_signature = api_signature

    @property
    def api_method(self):
        """Gets the api_method of this ApiIeMapping.


        :return: The api_method of this ApiIeMapping.
        :rtype: HttpMethod
        """
        return self._api_method

    @api_method.setter
    def api_method(self, api_method):
        """Sets the api_method of this ApiIeMapping.


        :param api_method: The api_method of this ApiIeMapping.
        :type api_method: HttpMethod
        """
        if api_method is None:
            raise ValueError("Invalid value for `api_method`, must not be `None`")  # noqa: E501

        self._api_method = api_method

    @property
    def ie_list(self):
        """Gets the ie_list of this ApiIeMapping.


        :return: The ie_list of this ApiIeMapping.
        :rtype: List[IeInfo]
        """
        return self._ie_list

    @ie_list.setter
    def ie_list(self, ie_list):
        """Sets the ie_list of this ApiIeMapping.


        :param ie_list: The ie_list of this ApiIeMapping.
        :type ie_list: List[IeInfo]
        """
        if ie_list is None:
            raise ValueError("Invalid value for `ie_list`, must not be `None`")  # noqa: E501

        self._ie_list = ie_list
