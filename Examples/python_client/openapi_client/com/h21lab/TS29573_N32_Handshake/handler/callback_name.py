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


class CallbackName(object):
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
        'callback_type': 'str'
    }

    attribute_map = {
        'callback_type': 'callbackType'
    }

    def __init__(self, callback_type=None, local_vars_configuration=None):  # noqa: E501
        """CallbackName - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._callback_type = None
        self.discriminator = None

        self.callback_type = callback_type

    @property
    def callback_type(self):
        """Gets the callback_type of this CallbackName.  # noqa: E501


        :return: The callback_type of this CallbackName.  # noqa: E501
        :rtype: str
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this CallbackName.


        :param callback_type: The callback_type of this CallbackName.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and callback_type is None:  # noqa: E501
            raise ValueError("Invalid value for `callback_type`, must not be `None`")  # noqa: E501

        self._callback_type = callback_type

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
        if not isinstance(other, CallbackName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallbackName):
            return True

        return self.to_dict() != other.to_dict()
