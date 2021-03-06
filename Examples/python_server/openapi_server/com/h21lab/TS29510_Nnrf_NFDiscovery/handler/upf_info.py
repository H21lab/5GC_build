# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atsss_capability import AtsssCapability
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.interface_upf_info_item import InterfaceUpfInfoItem
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pdu_session_type import PduSessionType
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai_upf_info_item import SnssaiUpfInfoItem
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tngf_info import TngfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.twif_info import TwifInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.w_agf_info import WAgfInfo
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atsss_capability import AtsssCapability  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.interface_upf_info_item import InterfaceUpfInfoItem  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pdu_session_type import PduSessionType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai_upf_info_item import SnssaiUpfInfoItem  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tngf_info import TngfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.twif_info import TwifInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.w_agf_info import WAgfInfo  # noqa: E501

class UpfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, s_nssai_upf_info_list=None, smf_serving_area=None, interface_upf_info_list=None, iwk_eps_ind=False, pdu_session_types=None, atsss_capability=None, ue_ip_addr_ind=False, tai_list=None, w_agf_info=None, tngf_info=None, twif_info=None, priority=None, redundant_gtpu=False):  # noqa: E501
        """UpfInfo - a model defined in OpenAPI

        :param s_nssai_upf_info_list: The s_nssai_upf_info_list of this UpfInfo.  # noqa: E501
        :type s_nssai_upf_info_list: List[SnssaiUpfInfoItem]
        :param smf_serving_area: The smf_serving_area of this UpfInfo.  # noqa: E501
        :type smf_serving_area: List[str]
        :param interface_upf_info_list: The interface_upf_info_list of this UpfInfo.  # noqa: E501
        :type interface_upf_info_list: List[InterfaceUpfInfoItem]
        :param iwk_eps_ind: The iwk_eps_ind of this UpfInfo.  # noqa: E501
        :type iwk_eps_ind: bool
        :param pdu_session_types: The pdu_session_types of this UpfInfo.  # noqa: E501
        :type pdu_session_types: List[PduSessionType]
        :param atsss_capability: The atsss_capability of this UpfInfo.  # noqa: E501
        :type atsss_capability: AtsssCapability
        :param ue_ip_addr_ind: The ue_ip_addr_ind of this UpfInfo.  # noqa: E501
        :type ue_ip_addr_ind: bool
        :param tai_list: The tai_list of this UpfInfo.  # noqa: E501
        :type tai_list: List[Tai]
        :param w_agf_info: The w_agf_info of this UpfInfo.  # noqa: E501
        :type w_agf_info: WAgfInfo
        :param tngf_info: The tngf_info of this UpfInfo.  # noqa: E501
        :type tngf_info: TngfInfo
        :param twif_info: The twif_info of this UpfInfo.  # noqa: E501
        :type twif_info: TwifInfo
        :param priority: The priority of this UpfInfo.  # noqa: E501
        :type priority: int
        :param redundant_gtpu: The redundant_gtpu of this UpfInfo.  # noqa: E501
        :type redundant_gtpu: bool
        """
        self.openapi_types = {
            's_nssai_upf_info_list': List[SnssaiUpfInfoItem],
            'smf_serving_area': List[str],
            'interface_upf_info_list': List[InterfaceUpfInfoItem],
            'iwk_eps_ind': bool,
            'pdu_session_types': List[PduSessionType],
            'atsss_capability': AtsssCapability,
            'ue_ip_addr_ind': bool,
            'tai_list': List[Tai],
            'w_agf_info': WAgfInfo,
            'tngf_info': TngfInfo,
            'twif_info': TwifInfo,
            'priority': int,
            'redundant_gtpu': bool
        }

        self.attribute_map = {
            's_nssai_upf_info_list': 'sNssaiUpfInfoList',
            'smf_serving_area': 'smfServingArea',
            'interface_upf_info_list': 'interfaceUpfInfoList',
            'iwk_eps_ind': 'iwkEpsInd',
            'pdu_session_types': 'pduSessionTypes',
            'atsss_capability': 'atsssCapability',
            'ue_ip_addr_ind': 'ueIpAddrInd',
            'tai_list': 'taiList',
            'w_agf_info': 'wAgfInfo',
            'tngf_info': 'tngfInfo',
            'twif_info': 'twifInfo',
            'priority': 'priority',
            'redundant_gtpu': 'redundantGtpu'
        }

        self._s_nssai_upf_info_list = s_nssai_upf_info_list
        self._smf_serving_area = smf_serving_area
        self._interface_upf_info_list = interface_upf_info_list
        self._iwk_eps_ind = iwk_eps_ind
        self._pdu_session_types = pdu_session_types
        self._atsss_capability = atsss_capability
        self._ue_ip_addr_ind = ue_ip_addr_ind
        self._tai_list = tai_list
        self._w_agf_info = w_agf_info
        self._tngf_info = tngf_info
        self._twif_info = twif_info
        self._priority = priority
        self._redundant_gtpu = redundant_gtpu

    @classmethod
    def from_dict(cls, dikt) -> 'UpfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpfInfo of this UpfInfo.  # noqa: E501
        :rtype: UpfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s_nssai_upf_info_list(self):
        """Gets the s_nssai_upf_info_list of this UpfInfo.


        :return: The s_nssai_upf_info_list of this UpfInfo.
        :rtype: List[SnssaiUpfInfoItem]
        """
        return self._s_nssai_upf_info_list

    @s_nssai_upf_info_list.setter
    def s_nssai_upf_info_list(self, s_nssai_upf_info_list):
        """Sets the s_nssai_upf_info_list of this UpfInfo.


        :param s_nssai_upf_info_list: The s_nssai_upf_info_list of this UpfInfo.
        :type s_nssai_upf_info_list: List[SnssaiUpfInfoItem]
        """
        if s_nssai_upf_info_list is None:
            raise ValueError("Invalid value for `s_nssai_upf_info_list`, must not be `None`")  # noqa: E501

        self._s_nssai_upf_info_list = s_nssai_upf_info_list

    @property
    def smf_serving_area(self):
        """Gets the smf_serving_area of this UpfInfo.


        :return: The smf_serving_area of this UpfInfo.
        :rtype: List[str]
        """
        return self._smf_serving_area

    @smf_serving_area.setter
    def smf_serving_area(self, smf_serving_area):
        """Sets the smf_serving_area of this UpfInfo.


        :param smf_serving_area: The smf_serving_area of this UpfInfo.
        :type smf_serving_area: List[str]
        """

        self._smf_serving_area = smf_serving_area

    @property
    def interface_upf_info_list(self):
        """Gets the interface_upf_info_list of this UpfInfo.


        :return: The interface_upf_info_list of this UpfInfo.
        :rtype: List[InterfaceUpfInfoItem]
        """
        return self._interface_upf_info_list

    @interface_upf_info_list.setter
    def interface_upf_info_list(self, interface_upf_info_list):
        """Sets the interface_upf_info_list of this UpfInfo.


        :param interface_upf_info_list: The interface_upf_info_list of this UpfInfo.
        :type interface_upf_info_list: List[InterfaceUpfInfoItem]
        """

        self._interface_upf_info_list = interface_upf_info_list

    @property
    def iwk_eps_ind(self):
        """Gets the iwk_eps_ind of this UpfInfo.


        :return: The iwk_eps_ind of this UpfInfo.
        :rtype: bool
        """
        return self._iwk_eps_ind

    @iwk_eps_ind.setter
    def iwk_eps_ind(self, iwk_eps_ind):
        """Sets the iwk_eps_ind of this UpfInfo.


        :param iwk_eps_ind: The iwk_eps_ind of this UpfInfo.
        :type iwk_eps_ind: bool
        """

        self._iwk_eps_ind = iwk_eps_ind

    @property
    def pdu_session_types(self):
        """Gets the pdu_session_types of this UpfInfo.


        :return: The pdu_session_types of this UpfInfo.
        :rtype: List[PduSessionType]
        """
        return self._pdu_session_types

    @pdu_session_types.setter
    def pdu_session_types(self, pdu_session_types):
        """Sets the pdu_session_types of this UpfInfo.


        :param pdu_session_types: The pdu_session_types of this UpfInfo.
        :type pdu_session_types: List[PduSessionType]
        """

        self._pdu_session_types = pdu_session_types

    @property
    def atsss_capability(self):
        """Gets the atsss_capability of this UpfInfo.


        :return: The atsss_capability of this UpfInfo.
        :rtype: AtsssCapability
        """
        return self._atsss_capability

    @atsss_capability.setter
    def atsss_capability(self, atsss_capability):
        """Sets the atsss_capability of this UpfInfo.


        :param atsss_capability: The atsss_capability of this UpfInfo.
        :type atsss_capability: AtsssCapability
        """

        self._atsss_capability = atsss_capability

    @property
    def ue_ip_addr_ind(self):
        """Gets the ue_ip_addr_ind of this UpfInfo.


        :return: The ue_ip_addr_ind of this UpfInfo.
        :rtype: bool
        """
        return self._ue_ip_addr_ind

    @ue_ip_addr_ind.setter
    def ue_ip_addr_ind(self, ue_ip_addr_ind):
        """Sets the ue_ip_addr_ind of this UpfInfo.


        :param ue_ip_addr_ind: The ue_ip_addr_ind of this UpfInfo.
        :type ue_ip_addr_ind: bool
        """

        self._ue_ip_addr_ind = ue_ip_addr_ind

    @property
    def tai_list(self):
        """Gets the tai_list of this UpfInfo.


        :return: The tai_list of this UpfInfo.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this UpfInfo.


        :param tai_list: The tai_list of this UpfInfo.
        :type tai_list: List[Tai]
        """

        self._tai_list = tai_list

    @property
    def w_agf_info(self):
        """Gets the w_agf_info of this UpfInfo.


        :return: The w_agf_info of this UpfInfo.
        :rtype: WAgfInfo
        """
        return self._w_agf_info

    @w_agf_info.setter
    def w_agf_info(self, w_agf_info):
        """Sets the w_agf_info of this UpfInfo.


        :param w_agf_info: The w_agf_info of this UpfInfo.
        :type w_agf_info: WAgfInfo
        """

        self._w_agf_info = w_agf_info

    @property
    def tngf_info(self):
        """Gets the tngf_info of this UpfInfo.


        :return: The tngf_info of this UpfInfo.
        :rtype: TngfInfo
        """
        return self._tngf_info

    @tngf_info.setter
    def tngf_info(self, tngf_info):
        """Sets the tngf_info of this UpfInfo.


        :param tngf_info: The tngf_info of this UpfInfo.
        :type tngf_info: TngfInfo
        """

        self._tngf_info = tngf_info

    @property
    def twif_info(self):
        """Gets the twif_info of this UpfInfo.


        :return: The twif_info of this UpfInfo.
        :rtype: TwifInfo
        """
        return self._twif_info

    @twif_info.setter
    def twif_info(self, twif_info):
        """Sets the twif_info of this UpfInfo.


        :param twif_info: The twif_info of this UpfInfo.
        :type twif_info: TwifInfo
        """

        self._twif_info = twif_info

    @property
    def priority(self):
        """Gets the priority of this UpfInfo.


        :return: The priority of this UpfInfo.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpfInfo.


        :param priority: The priority of this UpfInfo.
        :type priority: int
        """
        if priority is not None and priority > 65535:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `65535`")  # noqa: E501
        if priority is not None and priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._priority = priority

    @property
    def redundant_gtpu(self):
        """Gets the redundant_gtpu of this UpfInfo.


        :return: The redundant_gtpu of this UpfInfo.
        :rtype: bool
        """
        return self._redundant_gtpu

    @redundant_gtpu.setter
    def redundant_gtpu(self, redundant_gtpu):
        """Sets the redundant_gtpu of this UpfInfo.


        :param redundant_gtpu: The redundant_gtpu of this UpfInfo.
        :type redundant_gtpu: bool
        """

        self._redundant_gtpu = redundant_gtpu
