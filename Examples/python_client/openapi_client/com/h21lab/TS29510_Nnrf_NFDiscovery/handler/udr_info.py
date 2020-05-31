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


class UdrInfo(object):
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
        'group_id': 'str',
        'supi_ranges': 'list[SupiRange]',
        'gpsi_ranges': 'list[IdentityRange]',
        'external_group_identifiers_ranges': 'list[IdentityRange]',
        'supported_data_sets': 'list[DataSetId]'
    }

    attribute_map = {
        'group_id': 'groupId',
        'supi_ranges': 'supiRanges',
        'gpsi_ranges': 'gpsiRanges',
        'external_group_identifiers_ranges': 'externalGroupIdentifiersRanges',
        'supported_data_sets': 'supportedDataSets'
    }

    def __init__(self, group_id=None, supi_ranges=None, gpsi_ranges=None, external_group_identifiers_ranges=None, supported_data_sets=None, local_vars_configuration=None):  # noqa: E501
        """UdrInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_id = None
        self._supi_ranges = None
        self._gpsi_ranges = None
        self._external_group_identifiers_ranges = None
        self._supported_data_sets = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if supi_ranges is not None:
            self.supi_ranges = supi_ranges
        if gpsi_ranges is not None:
            self.gpsi_ranges = gpsi_ranges
        if external_group_identifiers_ranges is not None:
            self.external_group_identifiers_ranges = external_group_identifiers_ranges
        if supported_data_sets is not None:
            self.supported_data_sets = supported_data_sets

    @property
    def group_id(self):
        """Gets the group_id of this UdrInfo.  # noqa: E501


        :return: The group_id of this UdrInfo.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UdrInfo.


        :param group_id: The group_id of this UdrInfo.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def supi_ranges(self):
        """Gets the supi_ranges of this UdrInfo.  # noqa: E501


        :return: The supi_ranges of this UdrInfo.  # noqa: E501
        :rtype: list[SupiRange]
        """
        return self._supi_ranges

    @supi_ranges.setter
    def supi_ranges(self, supi_ranges):
        """Sets the supi_ranges of this UdrInfo.


        :param supi_ranges: The supi_ranges of this UdrInfo.  # noqa: E501
        :type: list[SupiRange]
        """

        self._supi_ranges = supi_ranges

    @property
    def gpsi_ranges(self):
        """Gets the gpsi_ranges of this UdrInfo.  # noqa: E501


        :return: The gpsi_ranges of this UdrInfo.  # noqa: E501
        :rtype: list[IdentityRange]
        """
        return self._gpsi_ranges

    @gpsi_ranges.setter
    def gpsi_ranges(self, gpsi_ranges):
        """Sets the gpsi_ranges of this UdrInfo.


        :param gpsi_ranges: The gpsi_ranges of this UdrInfo.  # noqa: E501
        :type: list[IdentityRange]
        """

        self._gpsi_ranges = gpsi_ranges

    @property
    def external_group_identifiers_ranges(self):
        """Gets the external_group_identifiers_ranges of this UdrInfo.  # noqa: E501


        :return: The external_group_identifiers_ranges of this UdrInfo.  # noqa: E501
        :rtype: list[IdentityRange]
        """
        return self._external_group_identifiers_ranges

    @external_group_identifiers_ranges.setter
    def external_group_identifiers_ranges(self, external_group_identifiers_ranges):
        """Sets the external_group_identifiers_ranges of this UdrInfo.


        :param external_group_identifiers_ranges: The external_group_identifiers_ranges of this UdrInfo.  # noqa: E501
        :type: list[IdentityRange]
        """

        self._external_group_identifiers_ranges = external_group_identifiers_ranges

    @property
    def supported_data_sets(self):
        """Gets the supported_data_sets of this UdrInfo.  # noqa: E501


        :return: The supported_data_sets of this UdrInfo.  # noqa: E501
        :rtype: list[DataSetId]
        """
        return self._supported_data_sets

    @supported_data_sets.setter
    def supported_data_sets(self, supported_data_sets):
        """Sets the supported_data_sets of this UdrInfo.


        :param supported_data_sets: The supported_data_sets of this UdrInfo.  # noqa: E501
        :type: list[DataSetId]
        """

        self._supported_data_sets = supported_data_sets

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
        if not isinstance(other, UdrInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UdrInfo):
            return True

        return self.to_dict() != other.to_dict()
