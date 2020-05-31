# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.identity_range import IdentityRange
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.supi_range import SupiRange
import re
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.identity_range import IdentityRange  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.supi_range import SupiRange  # noqa: E501
import re  # noqa: E501

class PcfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_id=None, dnn_list=None, supi_ranges=None, gpsi_ranges=None, rx_diam_host=None, rx_diam_realm=None, v2x_support_ind=False):  # noqa: E501
        """PcfInfo - a model defined in OpenAPI

        :param group_id: The group_id of this PcfInfo.  # noqa: E501
        :type group_id: str
        :param dnn_list: The dnn_list of this PcfInfo.  # noqa: E501
        :type dnn_list: List[str]
        :param supi_ranges: The supi_ranges of this PcfInfo.  # noqa: E501
        :type supi_ranges: List[SupiRange]
        :param gpsi_ranges: The gpsi_ranges of this PcfInfo.  # noqa: E501
        :type gpsi_ranges: List[IdentityRange]
        :param rx_diam_host: The rx_diam_host of this PcfInfo.  # noqa: E501
        :type rx_diam_host: str
        :param rx_diam_realm: The rx_diam_realm of this PcfInfo.  # noqa: E501
        :type rx_diam_realm: str
        :param v2x_support_ind: The v2x_support_ind of this PcfInfo.  # noqa: E501
        :type v2x_support_ind: bool
        """
        self.openapi_types = {
            'group_id': str,
            'dnn_list': List[str],
            'supi_ranges': List[SupiRange],
            'gpsi_ranges': List[IdentityRange],
            'rx_diam_host': str,
            'rx_diam_realm': str,
            'v2x_support_ind': bool
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'dnn_list': 'dnnList',
            'supi_ranges': 'supiRanges',
            'gpsi_ranges': 'gpsiRanges',
            'rx_diam_host': 'rxDiamHost',
            'rx_diam_realm': 'rxDiamRealm',
            'v2x_support_ind': 'v2xSupportInd'
        }

        self._group_id = group_id
        self._dnn_list = dnn_list
        self._supi_ranges = supi_ranges
        self._gpsi_ranges = gpsi_ranges
        self._rx_diam_host = rx_diam_host
        self._rx_diam_realm = rx_diam_realm
        self._v2x_support_ind = v2x_support_ind

    @classmethod
    def from_dict(cls, dikt) -> 'PcfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PcfInfo of this PcfInfo.  # noqa: E501
        :rtype: PcfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_id(self):
        """Gets the group_id of this PcfInfo.


        :return: The group_id of this PcfInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PcfInfo.


        :param group_id: The group_id of this PcfInfo.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def dnn_list(self):
        """Gets the dnn_list of this PcfInfo.


        :return: The dnn_list of this PcfInfo.
        :rtype: List[str]
        """
        return self._dnn_list

    @dnn_list.setter
    def dnn_list(self, dnn_list):
        """Sets the dnn_list of this PcfInfo.


        :param dnn_list: The dnn_list of this PcfInfo.
        :type dnn_list: List[str]
        """

        self._dnn_list = dnn_list

    @property
    def supi_ranges(self):
        """Gets the supi_ranges of this PcfInfo.


        :return: The supi_ranges of this PcfInfo.
        :rtype: List[SupiRange]
        """
        return self._supi_ranges

    @supi_ranges.setter
    def supi_ranges(self, supi_ranges):
        """Sets the supi_ranges of this PcfInfo.


        :param supi_ranges: The supi_ranges of this PcfInfo.
        :type supi_ranges: List[SupiRange]
        """

        self._supi_ranges = supi_ranges

    @property
    def gpsi_ranges(self):
        """Gets the gpsi_ranges of this PcfInfo.


        :return: The gpsi_ranges of this PcfInfo.
        :rtype: List[IdentityRange]
        """
        return self._gpsi_ranges

    @gpsi_ranges.setter
    def gpsi_ranges(self, gpsi_ranges):
        """Sets the gpsi_ranges of this PcfInfo.


        :param gpsi_ranges: The gpsi_ranges of this PcfInfo.
        :type gpsi_ranges: List[IdentityRange]
        """

        self._gpsi_ranges = gpsi_ranges

    @property
    def rx_diam_host(self):
        """Gets the rx_diam_host of this PcfInfo.


        :return: The rx_diam_host of this PcfInfo.
        :rtype: str
        """
        return self._rx_diam_host

    @rx_diam_host.setter
    def rx_diam_host(self, rx_diam_host):
        """Sets the rx_diam_host of this PcfInfo.


        :param rx_diam_host: The rx_diam_host of this PcfInfo.
        :type rx_diam_host: str
        """
        if rx_diam_host is not None and not re.search(r'^([A-Za-z0-9]+([-A-Za-z0-9]+)\.)+[a-z]{2,}$', rx_diam_host):  # noqa: E501
            raise ValueError("Invalid value for `rx_diam_host`, must be a follow pattern or equal to `/^([A-Za-z0-9]+([-A-Za-z0-9]+)\.)+[a-z]{2,}$/`")  # noqa: E501

        self._rx_diam_host = rx_diam_host

    @property
    def rx_diam_realm(self):
        """Gets the rx_diam_realm of this PcfInfo.


        :return: The rx_diam_realm of this PcfInfo.
        :rtype: str
        """
        return self._rx_diam_realm

    @rx_diam_realm.setter
    def rx_diam_realm(self, rx_diam_realm):
        """Sets the rx_diam_realm of this PcfInfo.


        :param rx_diam_realm: The rx_diam_realm of this PcfInfo.
        :type rx_diam_realm: str
        """
        if rx_diam_realm is not None and not re.search(r'^([A-Za-z0-9]+([-A-Za-z0-9]+)\.)+[a-z]{2,}$', rx_diam_realm):  # noqa: E501
            raise ValueError("Invalid value for `rx_diam_realm`, must be a follow pattern or equal to `/^([A-Za-z0-9]+([-A-Za-z0-9]+)\.)+[a-z]{2,}$/`")  # noqa: E501

        self._rx_diam_realm = rx_diam_realm

    @property
    def v2x_support_ind(self):
        """Gets the v2x_support_ind of this PcfInfo.


        :return: The v2x_support_ind of this PcfInfo.
        :rtype: bool
        """
        return self._v2x_support_ind

    @v2x_support_ind.setter
    def v2x_support_ind(self, v2x_support_ind):
        """Sets the v2x_support_ind of this PcfInfo.


        :param v2x_support_ind: The v2x_support_ind of this PcfInfo.
        :type v2x_support_ind: bool
        """

        self._v2x_support_ind = v2x_support_ind