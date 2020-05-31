# coding: utf-8

"""
    N32 Handshake API

    N32-c Handshake Service.  © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).  All rights reserved.   # noqa: E501

    The version of the OpenAPI document: 1.1.0.alpha-3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class IeInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ie_loc': 'IeLocation',
        'ie_type': 'IeType',
        'req_ie': 'str',
        'rsp_ie': 'str',
        'is_modifiable': 'bool'
    }

    attribute_map = {
        'ie_loc': 'ieLoc',
        'ie_type': 'ieType',
        'req_ie': 'reqIe',
        'rsp_ie': 'rspIe',
        'is_modifiable': 'isModifiable'
    }

    def __init__(self, ie_loc=None, ie_type=None, req_ie=None, rsp_ie=None, is_modifiable=None, local_vars_configuration=None):  # noqa: E501
        """IeInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ie_loc = None
        self._ie_type = None
        self._req_ie = None
        self._rsp_ie = None
        self._is_modifiable = None
        self.discriminator = None

        self.ie_loc = ie_loc
        self.ie_type = ie_type
        if req_ie is not None:
            self.req_ie = req_ie
        if rsp_ie is not None:
            self.rsp_ie = rsp_ie
        if is_modifiable is not None:
            self.is_modifiable = is_modifiable

    @property
    def ie_loc(self):
        """Gets the ie_loc of this IeInfo.  # noqa: E501


        :return: The ie_loc of this IeInfo.  # noqa: E501
        :rtype: IeLocation
        """
        return self._ie_loc

    @ie_loc.setter
    def ie_loc(self, ie_loc):
        """Sets the ie_loc of this IeInfo.


        :param ie_loc: The ie_loc of this IeInfo.  # noqa: E501
        :type: IeLocation
        """
        if self.local_vars_configuration.client_side_validation and ie_loc is None:  # noqa: E501
            raise ValueError("Invalid value for `ie_loc`, must not be `None`")  # noqa: E501

        self._ie_loc = ie_loc

    @property
    def ie_type(self):
        """Gets the ie_type of this IeInfo.  # noqa: E501


        :return: The ie_type of this IeInfo.  # noqa: E501
        :rtype: IeType
        """
        return self._ie_type

    @ie_type.setter
    def ie_type(self, ie_type):
        """Sets the ie_type of this IeInfo.


        :param ie_type: The ie_type of this IeInfo.  # noqa: E501
        :type: IeType
        """
        if self.local_vars_configuration.client_side_validation and ie_type is None:  # noqa: E501
            raise ValueError("Invalid value for `ie_type`, must not be `None`")  # noqa: E501

        self._ie_type = ie_type

    @property
    def req_ie(self):
        """Gets the req_ie of this IeInfo.  # noqa: E501


        :return: The req_ie of this IeInfo.  # noqa: E501
        :rtype: str
        """
        return self._req_ie

    @req_ie.setter
    def req_ie(self, req_ie):
        """Sets the req_ie of this IeInfo.


        :param req_ie: The req_ie of this IeInfo.  # noqa: E501
        :type: str
        """

        self._req_ie = req_ie

    @property
    def rsp_ie(self):
        """Gets the rsp_ie of this IeInfo.  # noqa: E501


        :return: The rsp_ie of this IeInfo.  # noqa: E501
        :rtype: str
        """
        return self._rsp_ie

    @rsp_ie.setter
    def rsp_ie(self, rsp_ie):
        """Sets the rsp_ie of this IeInfo.


        :param rsp_ie: The rsp_ie of this IeInfo.  # noqa: E501
        :type: str
        """

        self._rsp_ie = rsp_ie

    @property
    def is_modifiable(self):
        """Gets the is_modifiable of this IeInfo.  # noqa: E501


        :return: The is_modifiable of this IeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_modifiable

    @is_modifiable.setter
    def is_modifiable(self, is_modifiable):
        """Sets the is_modifiable of this IeInfo.


        :param is_modifiable: The is_modifiable of this IeInfo.  # noqa: E501
        :type: bool
        """

        self._is_modifiable = is_modifiable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IeInfo):
            return True

        return self.to_dict() != other.to_dict()