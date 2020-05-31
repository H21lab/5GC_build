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


class IpxProviderSecInfo(object):
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
        'ipx_provider_id': 'str',
        'raw_public_key_list': 'list[str]',
        'certificate_list': 'list[str]'
    }

    attribute_map = {
        'ipx_provider_id': 'ipxProviderId',
        'raw_public_key_list': 'rawPublicKeyList',
        'certificate_list': 'certificateList'
    }

    def __init__(self, ipx_provider_id=None, raw_public_key_list=None, certificate_list=None, local_vars_configuration=None):  # noqa: E501
        """IpxProviderSecInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ipx_provider_id = None
        self._raw_public_key_list = None
        self._certificate_list = None
        self.discriminator = None

        self.ipx_provider_id = ipx_provider_id
        if raw_public_key_list is not None:
            self.raw_public_key_list = raw_public_key_list
        if certificate_list is not None:
            self.certificate_list = certificate_list

    @property
    def ipx_provider_id(self):
        """Gets the ipx_provider_id of this IpxProviderSecInfo.  # noqa: E501

        Fully Qualified Domain Name  # noqa: E501

        :return: The ipx_provider_id of this IpxProviderSecInfo.  # noqa: E501
        :rtype: str
        """
        return self._ipx_provider_id

    @ipx_provider_id.setter
    def ipx_provider_id(self, ipx_provider_id):
        """Sets the ipx_provider_id of this IpxProviderSecInfo.

        Fully Qualified Domain Name  # noqa: E501

        :param ipx_provider_id: The ipx_provider_id of this IpxProviderSecInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ipx_provider_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ipx_provider_id`, must not be `None`")  # noqa: E501

        self._ipx_provider_id = ipx_provider_id

    @property
    def raw_public_key_list(self):
        """Gets the raw_public_key_list of this IpxProviderSecInfo.  # noqa: E501


        :return: The raw_public_key_list of this IpxProviderSecInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._raw_public_key_list

    @raw_public_key_list.setter
    def raw_public_key_list(self, raw_public_key_list):
        """Sets the raw_public_key_list of this IpxProviderSecInfo.


        :param raw_public_key_list: The raw_public_key_list of this IpxProviderSecInfo.  # noqa: E501
        :type: list[str]
        """

        self._raw_public_key_list = raw_public_key_list

    @property
    def certificate_list(self):
        """Gets the certificate_list of this IpxProviderSecInfo.  # noqa: E501


        :return: The certificate_list of this IpxProviderSecInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._certificate_list

    @certificate_list.setter
    def certificate_list(self, certificate_list):
        """Sets the certificate_list of this IpxProviderSecInfo.


        :param certificate_list: The certificate_list of this IpxProviderSecInfo.  # noqa: E501
        :type: list[str]
        """

        self._certificate_list = certificate_list

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
        if not isinstance(other, IpxProviderSecInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpxProviderSecInfo):
            return True

        return self.to_dict() != other.to_dict()
