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


class Dnf(object):
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
        'dnf_units': 'list[DnfUnit]'
    }

    attribute_map = {
        'dnf_units': 'dnfUnits'
    }

    def __init__(self, dnf_units=None, local_vars_configuration=None):  # noqa: E501
        """Dnf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dnf_units = None
        self.discriminator = None

        self.dnf_units = dnf_units

    @property
    def dnf_units(self):
        """Gets the dnf_units of this Dnf.  # noqa: E501


        :return: The dnf_units of this Dnf.  # noqa: E501
        :rtype: list[DnfUnit]
        """
        return self._dnf_units

    @dnf_units.setter
    def dnf_units(self, dnf_units):
        """Sets the dnf_units of this Dnf.


        :param dnf_units: The dnf_units of this Dnf.  # noqa: E501
        :type: list[DnfUnit]
        """
        if self.local_vars_configuration.client_side_validation and dnf_units is None:  # noqa: E501
            raise ValueError("Invalid value for `dnf_units`, must not be `None`")  # noqa: E501

        self._dnf_units = dnf_units

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
        if not isinstance(other, Dnf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dnf):
            return True

        return self.to_dict() != other.to_dict()
