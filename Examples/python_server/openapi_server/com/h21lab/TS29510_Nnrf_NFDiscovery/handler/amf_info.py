# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.guami import Guami
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.n2_interface_amf_info import N2InterfaceAmfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai_range import TaiRange
import re
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.guami import Guami  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.n2_interface_amf_info import N2InterfaceAmfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai_range import TaiRange  # noqa: E501
import re  # noqa: E501

class AmfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amf_set_id=None, amf_region_id=None, guami_list=None, tai_list=None, tai_range_list=None, backup_info_amf_failure=None, backup_info_amf_removal=None, n2_interface_amf_info=None):  # noqa: E501
        """AmfInfo - a model defined in OpenAPI

        :param amf_set_id: The amf_set_id of this AmfInfo.  # noqa: E501
        :type amf_set_id: str
        :param amf_region_id: The amf_region_id of this AmfInfo.  # noqa: E501
        :type amf_region_id: str
        :param guami_list: The guami_list of this AmfInfo.  # noqa: E501
        :type guami_list: List[Guami]
        :param tai_list: The tai_list of this AmfInfo.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this AmfInfo.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        :param backup_info_amf_failure: The backup_info_amf_failure of this AmfInfo.  # noqa: E501
        :type backup_info_amf_failure: List[Guami]
        :param backup_info_amf_removal: The backup_info_amf_removal of this AmfInfo.  # noqa: E501
        :type backup_info_amf_removal: List[Guami]
        :param n2_interface_amf_info: The n2_interface_amf_info of this AmfInfo.  # noqa: E501
        :type n2_interface_amf_info: N2InterfaceAmfInfo
        """
        self.openapi_types = {
            'amf_set_id': str,
            'amf_region_id': str,
            'guami_list': List[Guami],
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange],
            'backup_info_amf_failure': List[Guami],
            'backup_info_amf_removal': List[Guami],
            'n2_interface_amf_info': N2InterfaceAmfInfo
        }

        self.attribute_map = {
            'amf_set_id': 'amfSetId',
            'amf_region_id': 'amfRegionId',
            'guami_list': 'guamiList',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList',
            'backup_info_amf_failure': 'backupInfoAmfFailure',
            'backup_info_amf_removal': 'backupInfoAmfRemoval',
            'n2_interface_amf_info': 'n2InterfaceAmfInfo'
        }

        self._amf_set_id = amf_set_id
        self._amf_region_id = amf_region_id
        self._guami_list = guami_list
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list
        self._backup_info_amf_failure = backup_info_amf_failure
        self._backup_info_amf_removal = backup_info_amf_removal
        self._n2_interface_amf_info = n2_interface_amf_info

    @classmethod
    def from_dict(cls, dikt) -> 'AmfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfInfo of this AmfInfo.  # noqa: E501
        :rtype: AmfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amf_set_id(self):
        """Gets the amf_set_id of this AmfInfo.


        :return: The amf_set_id of this AmfInfo.
        :rtype: str
        """
        return self._amf_set_id

    @amf_set_id.setter
    def amf_set_id(self, amf_set_id):
        """Sets the amf_set_id of this AmfInfo.


        :param amf_set_id: The amf_set_id of this AmfInfo.
        :type amf_set_id: str
        """
        if amf_set_id is None:
            raise ValueError("Invalid value for `amf_set_id`, must not be `None`")  # noqa: E501
        if amf_set_id is not None and not re.search(r'^[0-3][A-Fa-f0-9]{2}$', amf_set_id):  # noqa: E501
            raise ValueError("Invalid value for `amf_set_id`, must be a follow pattern or equal to `/^[0-3][A-Fa-f0-9]{2}$/`")  # noqa: E501

        self._amf_set_id = amf_set_id

    @property
    def amf_region_id(self):
        """Gets the amf_region_id of this AmfInfo.


        :return: The amf_region_id of this AmfInfo.
        :rtype: str
        """
        return self._amf_region_id

    @amf_region_id.setter
    def amf_region_id(self, amf_region_id):
        """Sets the amf_region_id of this AmfInfo.


        :param amf_region_id: The amf_region_id of this AmfInfo.
        :type amf_region_id: str
        """
        if amf_region_id is None:
            raise ValueError("Invalid value for `amf_region_id`, must not be `None`")  # noqa: E501
        if amf_region_id is not None and not re.search(r'^[A-Fa-f0-9]{2}$', amf_region_id):  # noqa: E501
            raise ValueError("Invalid value for `amf_region_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{2}$/`")  # noqa: E501

        self._amf_region_id = amf_region_id

    @property
    def guami_list(self):
        """Gets the guami_list of this AmfInfo.


        :return: The guami_list of this AmfInfo.
        :rtype: List[Guami]
        """
        return self._guami_list

    @guami_list.setter
    def guami_list(self, guami_list):
        """Sets the guami_list of this AmfInfo.


        :param guami_list: The guami_list of this AmfInfo.
        :type guami_list: List[Guami]
        """
        if guami_list is None:
            raise ValueError("Invalid value for `guami_list`, must not be `None`")  # noqa: E501

        self._guami_list = guami_list

    @property
    def tai_list(self):
        """Gets the tai_list of this AmfInfo.


        :return: The tai_list of this AmfInfo.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this AmfInfo.


        :param tai_list: The tai_list of this AmfInfo.
        :type tai_list: List[Tai]
        """

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this AmfInfo.


        :return: The tai_range_list of this AmfInfo.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this AmfInfo.


        :param tai_range_list: The tai_range_list of this AmfInfo.
        :type tai_range_list: List[TaiRange]
        """

        self._tai_range_list = tai_range_list

    @property
    def backup_info_amf_failure(self):
        """Gets the backup_info_amf_failure of this AmfInfo.


        :return: The backup_info_amf_failure of this AmfInfo.
        :rtype: List[Guami]
        """
        return self._backup_info_amf_failure

    @backup_info_amf_failure.setter
    def backup_info_amf_failure(self, backup_info_amf_failure):
        """Sets the backup_info_amf_failure of this AmfInfo.


        :param backup_info_amf_failure: The backup_info_amf_failure of this AmfInfo.
        :type backup_info_amf_failure: List[Guami]
        """

        self._backup_info_amf_failure = backup_info_amf_failure

    @property
    def backup_info_amf_removal(self):
        """Gets the backup_info_amf_removal of this AmfInfo.


        :return: The backup_info_amf_removal of this AmfInfo.
        :rtype: List[Guami]
        """
        return self._backup_info_amf_removal

    @backup_info_amf_removal.setter
    def backup_info_amf_removal(self, backup_info_amf_removal):
        """Sets the backup_info_amf_removal of this AmfInfo.


        :param backup_info_amf_removal: The backup_info_amf_removal of this AmfInfo.
        :type backup_info_amf_removal: List[Guami]
        """

        self._backup_info_amf_removal = backup_info_amf_removal

    @property
    def n2_interface_amf_info(self):
        """Gets the n2_interface_amf_info of this AmfInfo.


        :return: The n2_interface_amf_info of this AmfInfo.
        :rtype: N2InterfaceAmfInfo
        """
        return self._n2_interface_amf_info

    @n2_interface_amf_info.setter
    def n2_interface_amf_info(self, n2_interface_amf_info):
        """Sets the n2_interface_amf_info of this AmfInfo.


        :param n2_interface_amf_info: The n2_interface_amf_info of this AmfInfo.
        :type n2_interface_amf_info: N2InterfaceAmfInfo
        """

        self._n2_interface_amf_info = n2_interface_amf_info
