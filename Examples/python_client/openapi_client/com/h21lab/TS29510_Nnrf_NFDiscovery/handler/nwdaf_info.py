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


class NwdafInfo(object):
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
        'event_ids': 'list[EventId]',
        'nwdaf_events': 'list[NwdafEvent]',
        'tai_list': 'list[Tai]',
        'tai_range_list': 'list[TaiRange]'
    }

    attribute_map = {
        'event_ids': 'eventIds',
        'nwdaf_events': 'nwdafEvents',
        'tai_list': 'taiList',
        'tai_range_list': 'taiRangeList'
    }

    def __init__(self, event_ids=None, nwdaf_events=None, tai_list=None, tai_range_list=None, local_vars_configuration=None):  # noqa: E501
        """NwdafInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_ids = None
        self._nwdaf_events = None
        self._tai_list = None
        self._tai_range_list = None
        self.discriminator = None

        if event_ids is not None:
            self.event_ids = event_ids
        if nwdaf_events is not None:
            self.nwdaf_events = nwdaf_events
        if tai_list is not None:
            self.tai_list = tai_list
        if tai_range_list is not None:
            self.tai_range_list = tai_range_list

    @property
    def event_ids(self):
        """Gets the event_ids of this NwdafInfo.  # noqa: E501


        :return: The event_ids of this NwdafInfo.  # noqa: E501
        :rtype: list[EventId]
        """
        return self._event_ids

    @event_ids.setter
    def event_ids(self, event_ids):
        """Sets the event_ids of this NwdafInfo.


        :param event_ids: The event_ids of this NwdafInfo.  # noqa: E501
        :type: list[EventId]
        """

        self._event_ids = event_ids

    @property
    def nwdaf_events(self):
        """Gets the nwdaf_events of this NwdafInfo.  # noqa: E501


        :return: The nwdaf_events of this NwdafInfo.  # noqa: E501
        :rtype: list[NwdafEvent]
        """
        return self._nwdaf_events

    @nwdaf_events.setter
    def nwdaf_events(self, nwdaf_events):
        """Sets the nwdaf_events of this NwdafInfo.


        :param nwdaf_events: The nwdaf_events of this NwdafInfo.  # noqa: E501
        :type: list[NwdafEvent]
        """

        self._nwdaf_events = nwdaf_events

    @property
    def tai_list(self):
        """Gets the tai_list of this NwdafInfo.  # noqa: E501


        :return: The tai_list of this NwdafInfo.  # noqa: E501
        :rtype: list[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this NwdafInfo.


        :param tai_list: The tai_list of this NwdafInfo.  # noqa: E501
        :type: list[Tai]
        """

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this NwdafInfo.  # noqa: E501


        :return: The tai_range_list of this NwdafInfo.  # noqa: E501
        :rtype: list[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this NwdafInfo.


        :param tai_range_list: The tai_range_list of this NwdafInfo.  # noqa: E501
        :type: list[TaiRange]
        """

        self._tai_range_list = tai_range_list

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
        if not isinstance(other, NwdafInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NwdafInfo):
            return True

        return self.to_dict() != other.to_dict()
