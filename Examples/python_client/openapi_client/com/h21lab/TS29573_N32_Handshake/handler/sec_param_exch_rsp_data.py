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


class SecParamExchRspData(object):
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
        'n32f_context_id': 'str',
        'selected_jwe_cipher_suite': 'str',
        'selected_jws_cipher_suite': 'str',
        'sel_protection_policy_info': 'ProtectionPolicy',
        'ipx_provider_sec_info_list': 'list[IpxProviderSecInfo]',
        'sender': 'str'
    }

    attribute_map = {
        'n32f_context_id': 'n32fContextId',
        'selected_jwe_cipher_suite': 'selectedJweCipherSuite',
        'selected_jws_cipher_suite': 'selectedJwsCipherSuite',
        'sel_protection_policy_info': 'selProtectionPolicyInfo',
        'ipx_provider_sec_info_list': 'ipxProviderSecInfoList',
        'sender': 'sender'
    }

    def __init__(self, n32f_context_id=None, selected_jwe_cipher_suite=None, selected_jws_cipher_suite=None, sel_protection_policy_info=None, ipx_provider_sec_info_list=None, sender=None, local_vars_configuration=None):  # noqa: E501
        """SecParamExchRspData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._n32f_context_id = None
        self._selected_jwe_cipher_suite = None
        self._selected_jws_cipher_suite = None
        self._sel_protection_policy_info = None
        self._ipx_provider_sec_info_list = None
        self._sender = None
        self.discriminator = None

        self.n32f_context_id = n32f_context_id
        if selected_jwe_cipher_suite is not None:
            self.selected_jwe_cipher_suite = selected_jwe_cipher_suite
        if selected_jws_cipher_suite is not None:
            self.selected_jws_cipher_suite = selected_jws_cipher_suite
        if sel_protection_policy_info is not None:
            self.sel_protection_policy_info = sel_protection_policy_info
        if ipx_provider_sec_info_list is not None:
            self.ipx_provider_sec_info_list = ipx_provider_sec_info_list
        if sender is not None:
            self.sender = sender

    @property
    def n32f_context_id(self):
        """Gets the n32f_context_id of this SecParamExchRspData.  # noqa: E501


        :return: The n32f_context_id of this SecParamExchRspData.  # noqa: E501
        :rtype: str
        """
        return self._n32f_context_id

    @n32f_context_id.setter
    def n32f_context_id(self, n32f_context_id):
        """Sets the n32f_context_id of this SecParamExchRspData.


        :param n32f_context_id: The n32f_context_id of this SecParamExchRspData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and n32f_context_id is None:  # noqa: E501
            raise ValueError("Invalid value for `n32f_context_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                n32f_context_id is not None and not re.search(r'^[A-Fa-f0-9]{16}$', n32f_context_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `n32f_context_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{16}$/`")  # noqa: E501

        self._n32f_context_id = n32f_context_id

    @property
    def selected_jwe_cipher_suite(self):
        """Gets the selected_jwe_cipher_suite of this SecParamExchRspData.  # noqa: E501


        :return: The selected_jwe_cipher_suite of this SecParamExchRspData.  # noqa: E501
        :rtype: str
        """
        return self._selected_jwe_cipher_suite

    @selected_jwe_cipher_suite.setter
    def selected_jwe_cipher_suite(self, selected_jwe_cipher_suite):
        """Sets the selected_jwe_cipher_suite of this SecParamExchRspData.


        :param selected_jwe_cipher_suite: The selected_jwe_cipher_suite of this SecParamExchRspData.  # noqa: E501
        :type: str
        """

        self._selected_jwe_cipher_suite = selected_jwe_cipher_suite

    @property
    def selected_jws_cipher_suite(self):
        """Gets the selected_jws_cipher_suite of this SecParamExchRspData.  # noqa: E501


        :return: The selected_jws_cipher_suite of this SecParamExchRspData.  # noqa: E501
        :rtype: str
        """
        return self._selected_jws_cipher_suite

    @selected_jws_cipher_suite.setter
    def selected_jws_cipher_suite(self, selected_jws_cipher_suite):
        """Sets the selected_jws_cipher_suite of this SecParamExchRspData.


        :param selected_jws_cipher_suite: The selected_jws_cipher_suite of this SecParamExchRspData.  # noqa: E501
        :type: str
        """

        self._selected_jws_cipher_suite = selected_jws_cipher_suite

    @property
    def sel_protection_policy_info(self):
        """Gets the sel_protection_policy_info of this SecParamExchRspData.  # noqa: E501


        :return: The sel_protection_policy_info of this SecParamExchRspData.  # noqa: E501
        :rtype: ProtectionPolicy
        """
        return self._sel_protection_policy_info

    @sel_protection_policy_info.setter
    def sel_protection_policy_info(self, sel_protection_policy_info):
        """Sets the sel_protection_policy_info of this SecParamExchRspData.


        :param sel_protection_policy_info: The sel_protection_policy_info of this SecParamExchRspData.  # noqa: E501
        :type: ProtectionPolicy
        """

        self._sel_protection_policy_info = sel_protection_policy_info

    @property
    def ipx_provider_sec_info_list(self):
        """Gets the ipx_provider_sec_info_list of this SecParamExchRspData.  # noqa: E501


        :return: The ipx_provider_sec_info_list of this SecParamExchRspData.  # noqa: E501
        :rtype: list[IpxProviderSecInfo]
        """
        return self._ipx_provider_sec_info_list

    @ipx_provider_sec_info_list.setter
    def ipx_provider_sec_info_list(self, ipx_provider_sec_info_list):
        """Sets the ipx_provider_sec_info_list of this SecParamExchRspData.


        :param ipx_provider_sec_info_list: The ipx_provider_sec_info_list of this SecParamExchRspData.  # noqa: E501
        :type: list[IpxProviderSecInfo]
        """

        self._ipx_provider_sec_info_list = ipx_provider_sec_info_list

    @property
    def sender(self):
        """Gets the sender of this SecParamExchRspData.  # noqa: E501

        Fully Qualified Domain Name  # noqa: E501

        :return: The sender of this SecParamExchRspData.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SecParamExchRspData.

        Fully Qualified Domain Name  # noqa: E501

        :param sender: The sender of this SecParamExchRspData.  # noqa: E501
        :type: str
        """

        self._sender = sender

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
        if not isinstance(other, SecParamExchRspData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecParamExchRspData):
            return True

        return self.to_dict() != other.to_dict()
