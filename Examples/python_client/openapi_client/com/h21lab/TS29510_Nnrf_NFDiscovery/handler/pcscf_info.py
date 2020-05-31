# coding: utf-8

"""
    NRF NFDiscovery Service

    NRF NFDiscovery Service. © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.   # noqa: E501

    The version of the OpenAPI document: 1.1.0.alpha-4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PcscfInfo(object):
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
        'access_type': 'list[AccessType]',
        'dnn_list': 'list[str]'
    }

    attribute_map = {
        'access_type': 'accessType',
        'dnn_list': 'dnnList'
    }

    def __init__(self, access_type=None, dnn_list=None, local_vars_configuration=None):  # noqa: E501
        """PcscfInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_type = None
        self._dnn_list = None
        self.discriminator = None

        if access_type is not None:
            self.access_type = access_type
        if dnn_list is not None:
            self.dnn_list = dnn_list

    @property
    def access_type(self):
        """Gets the access_type of this PcscfInfo.  # noqa: E501


        :return: The access_type of this PcscfInfo.  # noqa: E501
        :rtype: list[AccessType]
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this PcscfInfo.


        :param access_type: The access_type of this PcscfInfo.  # noqa: E501
        :type: list[AccessType]
        """

        self._access_type = access_type

    @property
    def dnn_list(self):
        """Gets the dnn_list of this PcscfInfo.  # noqa: E501


        :return: The dnn_list of this PcscfInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._dnn_list

    @dnn_list.setter
    def dnn_list(self, dnn_list):
        """Sets the dnn_list of this PcscfInfo.


        :param dnn_list: The dnn_list of this PcscfInfo.  # noqa: E501
        :type: list[str]
        """

        self._dnn_list = dnn_list

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
        if not isinstance(other, PcscfInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PcscfInfo):
            return True

        return self.to_dict() != other.to_dict()
