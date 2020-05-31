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


class PlmnSnssai(object):
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
        'plmn_id': 'PlmnId',
        's_nssai_list': 'list[Snssai]',
        'nid': 'str'
    }

    attribute_map = {
        'plmn_id': 'plmnId',
        's_nssai_list': 'sNssaiList',
        'nid': 'nid'
    }

    def __init__(self, plmn_id=None, s_nssai_list=None, nid=None, local_vars_configuration=None):  # noqa: E501
        """PlmnSnssai - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._plmn_id = None
        self._s_nssai_list = None
        self._nid = None
        self.discriminator = None

        self.plmn_id = plmn_id
        self.s_nssai_list = s_nssai_list
        if nid is not None:
            self.nid = nid

    @property
    def plmn_id(self):
        """Gets the plmn_id of this PlmnSnssai.  # noqa: E501


        :return: The plmn_id of this PlmnSnssai.  # noqa: E501
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this PlmnSnssai.


        :param plmn_id: The plmn_id of this PlmnSnssai.  # noqa: E501
        :type: PlmnId
        """
        if self.local_vars_configuration.client_side_validation and plmn_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def s_nssai_list(self):
        """Gets the s_nssai_list of this PlmnSnssai.  # noqa: E501


        :return: The s_nssai_list of this PlmnSnssai.  # noqa: E501
        :rtype: list[Snssai]
        """
        return self._s_nssai_list

    @s_nssai_list.setter
    def s_nssai_list(self, s_nssai_list):
        """Sets the s_nssai_list of this PlmnSnssai.


        :param s_nssai_list: The s_nssai_list of this PlmnSnssai.  # noqa: E501
        :type: list[Snssai]
        """
        if self.local_vars_configuration.client_side_validation and s_nssai_list is None:  # noqa: E501
            raise ValueError("Invalid value for `s_nssai_list`, must not be `None`")  # noqa: E501

        self._s_nssai_list = s_nssai_list

    @property
    def nid(self):
        """Gets the nid of this PlmnSnssai.  # noqa: E501


        :return: The nid of this PlmnSnssai.  # noqa: E501
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this PlmnSnssai.


        :param nid: The nid of this PlmnSnssai.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                nid is not None and not re.search(r'^[A-Fa-f0-9]{11}$', nid)):  # noqa: E501
            raise ValueError(r"Invalid value for `nid`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{11}$/`")  # noqa: E501

        self._nid = nid

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
        if not isinstance(other, PlmnSnssai):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlmnSnssai):
            return True

        return self.to_dict() != other.to_dict()
