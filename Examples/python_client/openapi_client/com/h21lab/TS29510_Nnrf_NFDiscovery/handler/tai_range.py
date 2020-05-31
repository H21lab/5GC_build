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


class TaiRange(object):
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
        'tac_range_list': 'list[TacRange]',
        'nid': 'str'
    }

    attribute_map = {
        'plmn_id': 'plmnId',
        'tac_range_list': 'tacRangeList',
        'nid': 'nid'
    }

    def __init__(self, plmn_id=None, tac_range_list=None, nid=None, local_vars_configuration=None):  # noqa: E501
        """TaiRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._plmn_id = None
        self._tac_range_list = None
        self._nid = None
        self.discriminator = None

        self.plmn_id = plmn_id
        self.tac_range_list = tac_range_list
        if nid is not None:
            self.nid = nid

    @property
    def plmn_id(self):
        """Gets the plmn_id of this TaiRange.  # noqa: E501


        :return: The plmn_id of this TaiRange.  # noqa: E501
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this TaiRange.


        :param plmn_id: The plmn_id of this TaiRange.  # noqa: E501
        :type: PlmnId
        """
        if self.local_vars_configuration.client_side_validation and plmn_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def tac_range_list(self):
        """Gets the tac_range_list of this TaiRange.  # noqa: E501


        :return: The tac_range_list of this TaiRange.  # noqa: E501
        :rtype: list[TacRange]
        """
        return self._tac_range_list

    @tac_range_list.setter
    def tac_range_list(self, tac_range_list):
        """Sets the tac_range_list of this TaiRange.


        :param tac_range_list: The tac_range_list of this TaiRange.  # noqa: E501
        :type: list[TacRange]
        """
        if self.local_vars_configuration.client_side_validation and tac_range_list is None:  # noqa: E501
            raise ValueError("Invalid value for `tac_range_list`, must not be `None`")  # noqa: E501

        self._tac_range_list = tac_range_list

    @property
    def nid(self):
        """Gets the nid of this TaiRange.  # noqa: E501


        :return: The nid of this TaiRange.  # noqa: E501
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this TaiRange.


        :param nid: The nid of this TaiRange.  # noqa: E501
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
        if not isinstance(other, TaiRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaiRange):
            return True

        return self.to_dict() != other.to_dict()
