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


class SecNegotiateRspData(object):
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
        'sender': 'str',
        'selected_sec_capability': 'SecurityCapability'
    }

    attribute_map = {
        'sender': 'sender',
        'selected_sec_capability': 'selectedSecCapability'
    }

    def __init__(self, sender=None, selected_sec_capability=None, local_vars_configuration=None):  # noqa: E501
        """SecNegotiateRspData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sender = None
        self._selected_sec_capability = None
        self.discriminator = None

        self.sender = sender
        self.selected_sec_capability = selected_sec_capability

    @property
    def sender(self):
        """Gets the sender of this SecNegotiateRspData.  # noqa: E501

        Fully Qualified Domain Name  # noqa: E501

        :return: The sender of this SecNegotiateRspData.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SecNegotiateRspData.

        Fully Qualified Domain Name  # noqa: E501

        :param sender: The sender of this SecNegotiateRspData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sender is None:  # noqa: E501
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def selected_sec_capability(self):
        """Gets the selected_sec_capability of this SecNegotiateRspData.  # noqa: E501


        :return: The selected_sec_capability of this SecNegotiateRspData.  # noqa: E501
        :rtype: SecurityCapability
        """
        return self._selected_sec_capability

    @selected_sec_capability.setter
    def selected_sec_capability(self, selected_sec_capability):
        """Sets the selected_sec_capability of this SecNegotiateRspData.


        :param selected_sec_capability: The selected_sec_capability of this SecNegotiateRspData.  # noqa: E501
        :type: SecurityCapability
        """
        if self.local_vars_configuration.client_side_validation and selected_sec_capability is None:  # noqa: E501
            raise ValueError("Invalid value for `selected_sec_capability`, must not be `None`")  # noqa: E501

        self._selected_sec_capability = selected_sec_capability

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
        if not isinstance(other, SecNegotiateRspData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecNegotiateRspData):
            return True

        return self.to_dict() != other.to_dict()
