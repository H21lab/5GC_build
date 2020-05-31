# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.supi_range import SupiRange
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.supi_range import SupiRange  # noqa: E501

class UdsfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_id=None, supi_ranges=None):  # noqa: E501
        """UdsfInfo - a model defined in OpenAPI

        :param group_id: The group_id of this UdsfInfo.  # noqa: E501
        :type group_id: str
        :param supi_ranges: The supi_ranges of this UdsfInfo.  # noqa: E501
        :type supi_ranges: List[SupiRange]
        """
        self.openapi_types = {
            'group_id': str,
            'supi_ranges': List[SupiRange]
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'supi_ranges': 'supiRanges'
        }

        self._group_id = group_id
        self._supi_ranges = supi_ranges

    @classmethod
    def from_dict(cls, dikt) -> 'UdsfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UdsfInfo of this UdsfInfo.  # noqa: E501
        :rtype: UdsfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_id(self):
        """Gets the group_id of this UdsfInfo.


        :return: The group_id of this UdsfInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UdsfInfo.


        :param group_id: The group_id of this UdsfInfo.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def supi_ranges(self):
        """Gets the supi_ranges of this UdsfInfo.


        :return: The supi_ranges of this UdsfInfo.
        :rtype: List[SupiRange]
        """
        return self._supi_ranges

    @supi_ranges.setter
    def supi_ranges(self, supi_ranges):
        """Sets the supi_ranges of this UdsfInfo.


        :param supi_ranges: The supi_ranges of this UdsfInfo.
        :type supi_ranges: List[SupiRange]
        """

        self._supi_ranges = supi_ranges
