# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.amf_info import AmfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ausf_info import AusfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.bsf_info import BsfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.chf_info import ChfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.default_notification_subscription import DefaultNotificationSubscription
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.gmlc_info import GmlcInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.hss_info import HssInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_addr import Ipv6Addr
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.lmf_info import LmfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_service import NFService
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_status import NFStatus
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_type import NFType
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nef_info import NefInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nwdaf_info import NwdafInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcf_info import PcfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcscf_info import PcscfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id import PlmnId
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id_nid import PlmnIdNid
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_snssai import PlmnSnssai
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.smf_info import SmfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai import Snssai
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udm_info import UdmInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udr_info import UdrInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udsf_info import UdsfInfo
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.upf_info import UpfInfo
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.amf_info import AmfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ausf_info import AusfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.bsf_info import BsfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.chf_info import ChfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.default_notification_subscription import DefaultNotificationSubscription  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.gmlc_info import GmlcInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.hss_info import HssInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_addr import Ipv6Addr  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.lmf_info import LmfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nef_info import NefInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_service import NFService  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_status import NFStatus  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_type import NFType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nwdaf_info import NwdafInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcf_info import PcfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcscf_info import PcscfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id import PlmnId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id_nid import PlmnIdNid  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_snssai import PlmnSnssai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.smf_info import SmfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai import Snssai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udm_info import UdmInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udr_info import UdrInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udsf_info import UdsfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.upf_info import UpfInfo  # noqa: E501

class NFProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nf_instance_id=None, nf_instance_name=None, nf_type=None, nf_status=None, plmn_list=None, s_nssais=None, per_plmn_snssai_list=None, nsi_list=None, fqdn=None, ipv4_addresses=None, ipv6_addresses=None, capacity=None, load=None, load_time_stamp=None, locality=None, priority=None, udr_info=None, udr_info_ext=None, udm_info=None, udm_info_ext=None, ausf_info=None, ausf_info_ext=None, amf_info=None, amf_info_ext=None, smf_info=None, smf_info_ext=None, upf_info=None, upf_info_ext=None, pcf_info=None, pcf_info_ext=None, bsf_info=None, bsf_info_ext=None, chf_info=None, chf_info_ext=None, udsf_info=None, udsf_info_ext=None, nwdaf_info=None, nef_info=None, pcscf_info=None, hss_info=None, custom_info=None, recovery_time=None, nf_service_persistence=False, nf_services=None, default_notification_subscriptions=None, lmf_info=None, gmlc_info=None, snpn_list=None, nf_set_id_list=None, serving_scope=None, lc_h_support_ind=False, olc_h_support_ind=False):  # noqa: E501
        """NFProfile - a model defined in OpenAPI

        :param nf_instance_id: The nf_instance_id of this NFProfile.  # noqa: E501
        :type nf_instance_id: str
        :param nf_instance_name: The nf_instance_name of this NFProfile.  # noqa: E501
        :type nf_instance_name: str
        :param nf_type: The nf_type of this NFProfile.  # noqa: E501
        :type nf_type: NFType
        :param nf_status: The nf_status of this NFProfile.  # noqa: E501
        :type nf_status: NFStatus
        :param plmn_list: The plmn_list of this NFProfile.  # noqa: E501
        :type plmn_list: List[PlmnId]
        :param s_nssais: The s_nssais of this NFProfile.  # noqa: E501
        :type s_nssais: List[Snssai]
        :param per_plmn_snssai_list: The per_plmn_snssai_list of this NFProfile.  # noqa: E501
        :type per_plmn_snssai_list: List[PlmnSnssai]
        :param nsi_list: The nsi_list of this NFProfile.  # noqa: E501
        :type nsi_list: List[str]
        :param fqdn: The fqdn of this NFProfile.  # noqa: E501
        :type fqdn: str
        :param ipv4_addresses: The ipv4_addresses of this NFProfile.  # noqa: E501
        :type ipv4_addresses: List[str]
        :param ipv6_addresses: The ipv6_addresses of this NFProfile.  # noqa: E501
        :type ipv6_addresses: List[Ipv6Addr]
        :param capacity: The capacity of this NFProfile.  # noqa: E501
        :type capacity: int
        :param load: The load of this NFProfile.  # noqa: E501
        :type load: int
        :param load_time_stamp: The load_time_stamp of this NFProfile.  # noqa: E501
        :type load_time_stamp: datetime
        :param locality: The locality of this NFProfile.  # noqa: E501
        :type locality: str
        :param priority: The priority of this NFProfile.  # noqa: E501
        :type priority: int
        :param udr_info: The udr_info of this NFProfile.  # noqa: E501
        :type udr_info: UdrInfo
        :param udr_info_ext: The udr_info_ext of this NFProfile.  # noqa: E501
        :type udr_info_ext: List[UdrInfo]
        :param udm_info: The udm_info of this NFProfile.  # noqa: E501
        :type udm_info: UdmInfo
        :param udm_info_ext: The udm_info_ext of this NFProfile.  # noqa: E501
        :type udm_info_ext: List[UdmInfo]
        :param ausf_info: The ausf_info of this NFProfile.  # noqa: E501
        :type ausf_info: AusfInfo
        :param ausf_info_ext: The ausf_info_ext of this NFProfile.  # noqa: E501
        :type ausf_info_ext: List[AusfInfo]
        :param amf_info: The amf_info of this NFProfile.  # noqa: E501
        :type amf_info: AmfInfo
        :param amf_info_ext: The amf_info_ext of this NFProfile.  # noqa: E501
        :type amf_info_ext: List[AmfInfo]
        :param smf_info: The smf_info of this NFProfile.  # noqa: E501
        :type smf_info: SmfInfo
        :param smf_info_ext: The smf_info_ext of this NFProfile.  # noqa: E501
        :type smf_info_ext: List[SmfInfo]
        :param upf_info: The upf_info of this NFProfile.  # noqa: E501
        :type upf_info: UpfInfo
        :param upf_info_ext: The upf_info_ext of this NFProfile.  # noqa: E501
        :type upf_info_ext: List[UpfInfo]
        :param pcf_info: The pcf_info of this NFProfile.  # noqa: E501
        :type pcf_info: PcfInfo
        :param pcf_info_ext: The pcf_info_ext of this NFProfile.  # noqa: E501
        :type pcf_info_ext: List[PcfInfo]
        :param bsf_info: The bsf_info of this NFProfile.  # noqa: E501
        :type bsf_info: BsfInfo
        :param bsf_info_ext: The bsf_info_ext of this NFProfile.  # noqa: E501
        :type bsf_info_ext: List[BsfInfo]
        :param chf_info: The chf_info of this NFProfile.  # noqa: E501
        :type chf_info: ChfInfo
        :param chf_info_ext: The chf_info_ext of this NFProfile.  # noqa: E501
        :type chf_info_ext: List[ChfInfo]
        :param udsf_info: The udsf_info of this NFProfile.  # noqa: E501
        :type udsf_info: UdsfInfo
        :param udsf_info_ext: The udsf_info_ext of this NFProfile.  # noqa: E501
        :type udsf_info_ext: List[UdsfInfo]
        :param nwdaf_info: The nwdaf_info of this NFProfile.  # noqa: E501
        :type nwdaf_info: NwdafInfo
        :param nef_info: The nef_info of this NFProfile.  # noqa: E501
        :type nef_info: NefInfo
        :param pcscf_info: The pcscf_info of this NFProfile.  # noqa: E501
        :type pcscf_info: List[PcscfInfo]
        :param hss_info: The hss_info of this NFProfile.  # noqa: E501
        :type hss_info: List[HssInfo]
        :param custom_info: The custom_info of this NFProfile.  # noqa: E501
        :type custom_info: object
        :param recovery_time: The recovery_time of this NFProfile.  # noqa: E501
        :type recovery_time: datetime
        :param nf_service_persistence: The nf_service_persistence of this NFProfile.  # noqa: E501
        :type nf_service_persistence: bool
        :param nf_services: The nf_services of this NFProfile.  # noqa: E501
        :type nf_services: List[NFService]
        :param default_notification_subscriptions: The default_notification_subscriptions of this NFProfile.  # noqa: E501
        :type default_notification_subscriptions: List[DefaultNotificationSubscription]
        :param lmf_info: The lmf_info of this NFProfile.  # noqa: E501
        :type lmf_info: LmfInfo
        :param gmlc_info: The gmlc_info of this NFProfile.  # noqa: E501
        :type gmlc_info: GmlcInfo
        :param snpn_list: The snpn_list of this NFProfile.  # noqa: E501
        :type snpn_list: List[PlmnIdNid]
        :param nf_set_id_list: The nf_set_id_list of this NFProfile.  # noqa: E501
        :type nf_set_id_list: List[str]
        :param serving_scope: The serving_scope of this NFProfile.  # noqa: E501
        :type serving_scope: List[str]
        :param lc_h_support_ind: The lc_h_support_ind of this NFProfile.  # noqa: E501
        :type lc_h_support_ind: bool
        :param olc_h_support_ind: The olc_h_support_ind of this NFProfile.  # noqa: E501
        :type olc_h_support_ind: bool
        """
        self.openapi_types = {
            'nf_instance_id': str,
            'nf_instance_name': str,
            'nf_type': NFType,
            'nf_status': NFStatus,
            'plmn_list': List[PlmnId],
            's_nssais': List[Snssai],
            'per_plmn_snssai_list': List[PlmnSnssai],
            'nsi_list': List[str],
            'fqdn': str,
            'ipv4_addresses': List[str],
            'ipv6_addresses': List[Ipv6Addr],
            'capacity': int,
            'load': int,
            'load_time_stamp': datetime,
            'locality': str,
            'priority': int,
            'udr_info': UdrInfo,
            'udr_info_ext': List[UdrInfo],
            'udm_info': UdmInfo,
            'udm_info_ext': List[UdmInfo],
            'ausf_info': AusfInfo,
            'ausf_info_ext': List[AusfInfo],
            'amf_info': AmfInfo,
            'amf_info_ext': List[AmfInfo],
            'smf_info': SmfInfo,
            'smf_info_ext': List[SmfInfo],
            'upf_info': UpfInfo,
            'upf_info_ext': List[UpfInfo],
            'pcf_info': PcfInfo,
            'pcf_info_ext': List[PcfInfo],
            'bsf_info': BsfInfo,
            'bsf_info_ext': List[BsfInfo],
            'chf_info': ChfInfo,
            'chf_info_ext': List[ChfInfo],
            'udsf_info': UdsfInfo,
            'udsf_info_ext': List[UdsfInfo],
            'nwdaf_info': NwdafInfo,
            'nef_info': NefInfo,
            'pcscf_info': List[PcscfInfo],
            'hss_info': List[HssInfo],
            'custom_info': object,
            'recovery_time': datetime,
            'nf_service_persistence': bool,
            'nf_services': List[NFService],
            'default_notification_subscriptions': List[DefaultNotificationSubscription],
            'lmf_info': LmfInfo,
            'gmlc_info': GmlcInfo,
            'snpn_list': List[PlmnIdNid],
            'nf_set_id_list': List[str],
            'serving_scope': List[str],
            'lc_h_support_ind': bool,
            'olc_h_support_ind': bool
        }

        self.attribute_map = {
            'nf_instance_id': 'nfInstanceId',
            'nf_instance_name': 'nfInstanceName',
            'nf_type': 'nfType',
            'nf_status': 'nfStatus',
            'plmn_list': 'plmnList',
            's_nssais': 'sNssais',
            'per_plmn_snssai_list': 'perPlmnSnssaiList',
            'nsi_list': 'nsiList',
            'fqdn': 'fqdn',
            'ipv4_addresses': 'ipv4Addresses',
            'ipv6_addresses': 'ipv6Addresses',
            'capacity': 'capacity',
            'load': 'load',
            'load_time_stamp': 'loadTimeStamp',
            'locality': 'locality',
            'priority': 'priority',
            'udr_info': 'udrInfo',
            'udr_info_ext': 'udrInfoExt',
            'udm_info': 'udmInfo',
            'udm_info_ext': 'udmInfoExt',
            'ausf_info': 'ausfInfo',
            'ausf_info_ext': 'ausfInfoExt',
            'amf_info': 'amfInfo',
            'amf_info_ext': 'amfInfoExt',
            'smf_info': 'smfInfo',
            'smf_info_ext': 'smfInfoExt',
            'upf_info': 'upfInfo',
            'upf_info_ext': 'upfInfoExt',
            'pcf_info': 'pcfInfo',
            'pcf_info_ext': 'pcfInfoExt',
            'bsf_info': 'bsfInfo',
            'bsf_info_ext': 'bsfInfoExt',
            'chf_info': 'chfInfo',
            'chf_info_ext': 'chfInfoExt',
            'udsf_info': 'udsfInfo',
            'udsf_info_ext': 'udsfInfoExt',
            'nwdaf_info': 'nwdafInfo',
            'nef_info': 'nefInfo',
            'pcscf_info': 'pcscfInfo',
            'hss_info': 'hssInfo',
            'custom_info': 'customInfo',
            'recovery_time': 'recoveryTime',
            'nf_service_persistence': 'nfServicePersistence',
            'nf_services': 'nfServices',
            'default_notification_subscriptions': 'defaultNotificationSubscriptions',
            'lmf_info': 'lmfInfo',
            'gmlc_info': 'gmlcInfo',
            'snpn_list': 'snpnList',
            'nf_set_id_list': 'nfSetIdList',
            'serving_scope': 'servingScope',
            'lc_h_support_ind': 'lcHSupportInd',
            'olc_h_support_ind': 'olcHSupportInd'
        }

        self._nf_instance_id = nf_instance_id
        self._nf_instance_name = nf_instance_name
        self._nf_type = nf_type
        self._nf_status = nf_status
        self._plmn_list = plmn_list
        self._s_nssais = s_nssais
        self._per_plmn_snssai_list = per_plmn_snssai_list
        self._nsi_list = nsi_list
        self._fqdn = fqdn
        self._ipv4_addresses = ipv4_addresses
        self._ipv6_addresses = ipv6_addresses
        self._capacity = capacity
        self._load = load
        self._load_time_stamp = load_time_stamp
        self._locality = locality
        self._priority = priority
        self._udr_info = udr_info
        self._udr_info_ext = udr_info_ext
        self._udm_info = udm_info
        self._udm_info_ext = udm_info_ext
        self._ausf_info = ausf_info
        self._ausf_info_ext = ausf_info_ext
        self._amf_info = amf_info
        self._amf_info_ext = amf_info_ext
        self._smf_info = smf_info
        self._smf_info_ext = smf_info_ext
        self._upf_info = upf_info
        self._upf_info_ext = upf_info_ext
        self._pcf_info = pcf_info
        self._pcf_info_ext = pcf_info_ext
        self._bsf_info = bsf_info
        self._bsf_info_ext = bsf_info_ext
        self._chf_info = chf_info
        self._chf_info_ext = chf_info_ext
        self._udsf_info = udsf_info
        self._udsf_info_ext = udsf_info_ext
        self._nwdaf_info = nwdaf_info
        self._nef_info = nef_info
        self._pcscf_info = pcscf_info
        self._hss_info = hss_info
        self._custom_info = custom_info
        self._recovery_time = recovery_time
        self._nf_service_persistence = nf_service_persistence
        self._nf_services = nf_services
        self._default_notification_subscriptions = default_notification_subscriptions
        self._lmf_info = lmf_info
        self._gmlc_info = gmlc_info
        self._snpn_list = snpn_list
        self._nf_set_id_list = nf_set_id_list
        self._serving_scope = serving_scope
        self._lc_h_support_ind = lc_h_support_ind
        self._olc_h_support_ind = olc_h_support_ind

    @classmethod
    def from_dict(cls, dikt) -> 'NFProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NFProfile of this NFProfile.  # noqa: E501
        :rtype: NFProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nf_instance_id(self):
        """Gets the nf_instance_id of this NFProfile.


        :return: The nf_instance_id of this NFProfile.
        :rtype: str
        """
        return self._nf_instance_id

    @nf_instance_id.setter
    def nf_instance_id(self, nf_instance_id):
        """Sets the nf_instance_id of this NFProfile.


        :param nf_instance_id: The nf_instance_id of this NFProfile.
        :type nf_instance_id: str
        """
        if nf_instance_id is None:
            raise ValueError("Invalid value for `nf_instance_id`, must not be `None`")  # noqa: E501

        self._nf_instance_id = nf_instance_id

    @property
    def nf_instance_name(self):
        """Gets the nf_instance_name of this NFProfile.


        :return: The nf_instance_name of this NFProfile.
        :rtype: str
        """
        return self._nf_instance_name

    @nf_instance_name.setter
    def nf_instance_name(self, nf_instance_name):
        """Sets the nf_instance_name of this NFProfile.


        :param nf_instance_name: The nf_instance_name of this NFProfile.
        :type nf_instance_name: str
        """

        self._nf_instance_name = nf_instance_name

    @property
    def nf_type(self):
        """Gets the nf_type of this NFProfile.


        :return: The nf_type of this NFProfile.
        :rtype: NFType
        """
        return self._nf_type

    @nf_type.setter
    def nf_type(self, nf_type):
        """Sets the nf_type of this NFProfile.


        :param nf_type: The nf_type of this NFProfile.
        :type nf_type: NFType
        """
        if nf_type is None:
            raise ValueError("Invalid value for `nf_type`, must not be `None`")  # noqa: E501

        self._nf_type = nf_type

    @property
    def nf_status(self):
        """Gets the nf_status of this NFProfile.


        :return: The nf_status of this NFProfile.
        :rtype: NFStatus
        """
        return self._nf_status

    @nf_status.setter
    def nf_status(self, nf_status):
        """Sets the nf_status of this NFProfile.


        :param nf_status: The nf_status of this NFProfile.
        :type nf_status: NFStatus
        """
        if nf_status is None:
            raise ValueError("Invalid value for `nf_status`, must not be `None`")  # noqa: E501

        self._nf_status = nf_status

    @property
    def plmn_list(self):
        """Gets the plmn_list of this NFProfile.


        :return: The plmn_list of this NFProfile.
        :rtype: List[PlmnId]
        """
        return self._plmn_list

    @plmn_list.setter
    def plmn_list(self, plmn_list):
        """Sets the plmn_list of this NFProfile.


        :param plmn_list: The plmn_list of this NFProfile.
        :type plmn_list: List[PlmnId]
        """

        self._plmn_list = plmn_list

    @property
    def s_nssais(self):
        """Gets the s_nssais of this NFProfile.


        :return: The s_nssais of this NFProfile.
        :rtype: List[Snssai]
        """
        return self._s_nssais

    @s_nssais.setter
    def s_nssais(self, s_nssais):
        """Sets the s_nssais of this NFProfile.


        :param s_nssais: The s_nssais of this NFProfile.
        :type s_nssais: List[Snssai]
        """

        self._s_nssais = s_nssais

    @property
    def per_plmn_snssai_list(self):
        """Gets the per_plmn_snssai_list of this NFProfile.


        :return: The per_plmn_snssai_list of this NFProfile.
        :rtype: List[PlmnSnssai]
        """
        return self._per_plmn_snssai_list

    @per_plmn_snssai_list.setter
    def per_plmn_snssai_list(self, per_plmn_snssai_list):
        """Sets the per_plmn_snssai_list of this NFProfile.


        :param per_plmn_snssai_list: The per_plmn_snssai_list of this NFProfile.
        :type per_plmn_snssai_list: List[PlmnSnssai]
        """

        self._per_plmn_snssai_list = per_plmn_snssai_list

    @property
    def nsi_list(self):
        """Gets the nsi_list of this NFProfile.


        :return: The nsi_list of this NFProfile.
        :rtype: List[str]
        """
        return self._nsi_list

    @nsi_list.setter
    def nsi_list(self, nsi_list):
        """Sets the nsi_list of this NFProfile.


        :param nsi_list: The nsi_list of this NFProfile.
        :type nsi_list: List[str]
        """

        self._nsi_list = nsi_list

    @property
    def fqdn(self):
        """Gets the fqdn of this NFProfile.

        Fully Qualified Domain Name  # noqa: E501

        :return: The fqdn of this NFProfile.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this NFProfile.

        Fully Qualified Domain Name  # noqa: E501

        :param fqdn: The fqdn of this NFProfile.
        :type fqdn: str
        """

        self._fqdn = fqdn

    @property
    def ipv4_addresses(self):
        """Gets the ipv4_addresses of this NFProfile.


        :return: The ipv4_addresses of this NFProfile.
        :rtype: List[str]
        """
        return self._ipv4_addresses

    @ipv4_addresses.setter
    def ipv4_addresses(self, ipv4_addresses):
        """Sets the ipv4_addresses of this NFProfile.


        :param ipv4_addresses: The ipv4_addresses of this NFProfile.
        :type ipv4_addresses: List[str]
        """

        self._ipv4_addresses = ipv4_addresses

    @property
    def ipv6_addresses(self):
        """Gets the ipv6_addresses of this NFProfile.


        :return: The ipv6_addresses of this NFProfile.
        :rtype: List[Ipv6Addr]
        """
        return self._ipv6_addresses

    @ipv6_addresses.setter
    def ipv6_addresses(self, ipv6_addresses):
        """Sets the ipv6_addresses of this NFProfile.


        :param ipv6_addresses: The ipv6_addresses of this NFProfile.
        :type ipv6_addresses: List[Ipv6Addr]
        """

        self._ipv6_addresses = ipv6_addresses

    @property
    def capacity(self):
        """Gets the capacity of this NFProfile.


        :return: The capacity of this NFProfile.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this NFProfile.


        :param capacity: The capacity of this NFProfile.
        :type capacity: int
        """
        if capacity is not None and capacity > 65535:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value less than or equal to `65535`")  # noqa: E501
        if capacity is not None and capacity < 0:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity = capacity

    @property
    def load(self):
        """Gets the load of this NFProfile.


        :return: The load of this NFProfile.
        :rtype: int
        """
        return self._load

    @load.setter
    def load(self, load):
        """Sets the load of this NFProfile.


        :param load: The load of this NFProfile.
        :type load: int
        """
        if load is not None and load > 100:  # noqa: E501
            raise ValueError("Invalid value for `load`, must be a value less than or equal to `100`")  # noqa: E501
        if load is not None and load < 0:  # noqa: E501
            raise ValueError("Invalid value for `load`, must be a value greater than or equal to `0`")  # noqa: E501

        self._load = load

    @property
    def load_time_stamp(self):
        """Gets the load_time_stamp of this NFProfile.


        :return: The load_time_stamp of this NFProfile.
        :rtype: datetime
        """
        return self._load_time_stamp

    @load_time_stamp.setter
    def load_time_stamp(self, load_time_stamp):
        """Sets the load_time_stamp of this NFProfile.


        :param load_time_stamp: The load_time_stamp of this NFProfile.
        :type load_time_stamp: datetime
        """

        self._load_time_stamp = load_time_stamp

    @property
    def locality(self):
        """Gets the locality of this NFProfile.


        :return: The locality of this NFProfile.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this NFProfile.


        :param locality: The locality of this NFProfile.
        :type locality: str
        """

        self._locality = locality

    @property
    def priority(self):
        """Gets the priority of this NFProfile.


        :return: The priority of this NFProfile.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NFProfile.


        :param priority: The priority of this NFProfile.
        :type priority: int
        """
        if priority is not None and priority > 65535:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `65535`")  # noqa: E501
        if priority is not None and priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._priority = priority

    @property
    def udr_info(self):
        """Gets the udr_info of this NFProfile.


        :return: The udr_info of this NFProfile.
        :rtype: UdrInfo
        """
        return self._udr_info

    @udr_info.setter
    def udr_info(self, udr_info):
        """Sets the udr_info of this NFProfile.


        :param udr_info: The udr_info of this NFProfile.
        :type udr_info: UdrInfo
        """

        self._udr_info = udr_info

    @property
    def udr_info_ext(self):
        """Gets the udr_info_ext of this NFProfile.


        :return: The udr_info_ext of this NFProfile.
        :rtype: List[UdrInfo]
        """
        return self._udr_info_ext

    @udr_info_ext.setter
    def udr_info_ext(self, udr_info_ext):
        """Sets the udr_info_ext of this NFProfile.


        :param udr_info_ext: The udr_info_ext of this NFProfile.
        :type udr_info_ext: List[UdrInfo]
        """

        self._udr_info_ext = udr_info_ext

    @property
    def udm_info(self):
        """Gets the udm_info of this NFProfile.


        :return: The udm_info of this NFProfile.
        :rtype: UdmInfo
        """
        return self._udm_info

    @udm_info.setter
    def udm_info(self, udm_info):
        """Sets the udm_info of this NFProfile.


        :param udm_info: The udm_info of this NFProfile.
        :type udm_info: UdmInfo
        """

        self._udm_info = udm_info

    @property
    def udm_info_ext(self):
        """Gets the udm_info_ext of this NFProfile.


        :return: The udm_info_ext of this NFProfile.
        :rtype: List[UdmInfo]
        """
        return self._udm_info_ext

    @udm_info_ext.setter
    def udm_info_ext(self, udm_info_ext):
        """Sets the udm_info_ext of this NFProfile.


        :param udm_info_ext: The udm_info_ext of this NFProfile.
        :type udm_info_ext: List[UdmInfo]
        """

        self._udm_info_ext = udm_info_ext

    @property
    def ausf_info(self):
        """Gets the ausf_info of this NFProfile.


        :return: The ausf_info of this NFProfile.
        :rtype: AusfInfo
        """
        return self._ausf_info

    @ausf_info.setter
    def ausf_info(self, ausf_info):
        """Sets the ausf_info of this NFProfile.


        :param ausf_info: The ausf_info of this NFProfile.
        :type ausf_info: AusfInfo
        """

        self._ausf_info = ausf_info

    @property
    def ausf_info_ext(self):
        """Gets the ausf_info_ext of this NFProfile.


        :return: The ausf_info_ext of this NFProfile.
        :rtype: List[AusfInfo]
        """
        return self._ausf_info_ext

    @ausf_info_ext.setter
    def ausf_info_ext(self, ausf_info_ext):
        """Sets the ausf_info_ext of this NFProfile.


        :param ausf_info_ext: The ausf_info_ext of this NFProfile.
        :type ausf_info_ext: List[AusfInfo]
        """

        self._ausf_info_ext = ausf_info_ext

    @property
    def amf_info(self):
        """Gets the amf_info of this NFProfile.


        :return: The amf_info of this NFProfile.
        :rtype: AmfInfo
        """
        return self._amf_info

    @amf_info.setter
    def amf_info(self, amf_info):
        """Sets the amf_info of this NFProfile.


        :param amf_info: The amf_info of this NFProfile.
        :type amf_info: AmfInfo
        """

        self._amf_info = amf_info

    @property
    def amf_info_ext(self):
        """Gets the amf_info_ext of this NFProfile.


        :return: The amf_info_ext of this NFProfile.
        :rtype: List[AmfInfo]
        """
        return self._amf_info_ext

    @amf_info_ext.setter
    def amf_info_ext(self, amf_info_ext):
        """Sets the amf_info_ext of this NFProfile.


        :param amf_info_ext: The amf_info_ext of this NFProfile.
        :type amf_info_ext: List[AmfInfo]
        """

        self._amf_info_ext = amf_info_ext

    @property
    def smf_info(self):
        """Gets the smf_info of this NFProfile.


        :return: The smf_info of this NFProfile.
        :rtype: SmfInfo
        """
        return self._smf_info

    @smf_info.setter
    def smf_info(self, smf_info):
        """Sets the smf_info of this NFProfile.


        :param smf_info: The smf_info of this NFProfile.
        :type smf_info: SmfInfo
        """

        self._smf_info = smf_info

    @property
    def smf_info_ext(self):
        """Gets the smf_info_ext of this NFProfile.


        :return: The smf_info_ext of this NFProfile.
        :rtype: List[SmfInfo]
        """
        return self._smf_info_ext

    @smf_info_ext.setter
    def smf_info_ext(self, smf_info_ext):
        """Sets the smf_info_ext of this NFProfile.


        :param smf_info_ext: The smf_info_ext of this NFProfile.
        :type smf_info_ext: List[SmfInfo]
        """

        self._smf_info_ext = smf_info_ext

    @property
    def upf_info(self):
        """Gets the upf_info of this NFProfile.


        :return: The upf_info of this NFProfile.
        :rtype: UpfInfo
        """
        return self._upf_info

    @upf_info.setter
    def upf_info(self, upf_info):
        """Sets the upf_info of this NFProfile.


        :param upf_info: The upf_info of this NFProfile.
        :type upf_info: UpfInfo
        """

        self._upf_info = upf_info

    @property
    def upf_info_ext(self):
        """Gets the upf_info_ext of this NFProfile.


        :return: The upf_info_ext of this NFProfile.
        :rtype: List[UpfInfo]
        """
        return self._upf_info_ext

    @upf_info_ext.setter
    def upf_info_ext(self, upf_info_ext):
        """Sets the upf_info_ext of this NFProfile.


        :param upf_info_ext: The upf_info_ext of this NFProfile.
        :type upf_info_ext: List[UpfInfo]
        """

        self._upf_info_ext = upf_info_ext

    @property
    def pcf_info(self):
        """Gets the pcf_info of this NFProfile.


        :return: The pcf_info of this NFProfile.
        :rtype: PcfInfo
        """
        return self._pcf_info

    @pcf_info.setter
    def pcf_info(self, pcf_info):
        """Sets the pcf_info of this NFProfile.


        :param pcf_info: The pcf_info of this NFProfile.
        :type pcf_info: PcfInfo
        """

        self._pcf_info = pcf_info

    @property
    def pcf_info_ext(self):
        """Gets the pcf_info_ext of this NFProfile.


        :return: The pcf_info_ext of this NFProfile.
        :rtype: List[PcfInfo]
        """
        return self._pcf_info_ext

    @pcf_info_ext.setter
    def pcf_info_ext(self, pcf_info_ext):
        """Sets the pcf_info_ext of this NFProfile.


        :param pcf_info_ext: The pcf_info_ext of this NFProfile.
        :type pcf_info_ext: List[PcfInfo]
        """

        self._pcf_info_ext = pcf_info_ext

    @property
    def bsf_info(self):
        """Gets the bsf_info of this NFProfile.


        :return: The bsf_info of this NFProfile.
        :rtype: BsfInfo
        """
        return self._bsf_info

    @bsf_info.setter
    def bsf_info(self, bsf_info):
        """Sets the bsf_info of this NFProfile.


        :param bsf_info: The bsf_info of this NFProfile.
        :type bsf_info: BsfInfo
        """

        self._bsf_info = bsf_info

    @property
    def bsf_info_ext(self):
        """Gets the bsf_info_ext of this NFProfile.


        :return: The bsf_info_ext of this NFProfile.
        :rtype: List[BsfInfo]
        """
        return self._bsf_info_ext

    @bsf_info_ext.setter
    def bsf_info_ext(self, bsf_info_ext):
        """Sets the bsf_info_ext of this NFProfile.


        :param bsf_info_ext: The bsf_info_ext of this NFProfile.
        :type bsf_info_ext: List[BsfInfo]
        """

        self._bsf_info_ext = bsf_info_ext

    @property
    def chf_info(self):
        """Gets the chf_info of this NFProfile.


        :return: The chf_info of this NFProfile.
        :rtype: ChfInfo
        """
        return self._chf_info

    @chf_info.setter
    def chf_info(self, chf_info):
        """Sets the chf_info of this NFProfile.


        :param chf_info: The chf_info of this NFProfile.
        :type chf_info: ChfInfo
        """

        self._chf_info = chf_info

    @property
    def chf_info_ext(self):
        """Gets the chf_info_ext of this NFProfile.


        :return: The chf_info_ext of this NFProfile.
        :rtype: List[ChfInfo]
        """
        return self._chf_info_ext

    @chf_info_ext.setter
    def chf_info_ext(self, chf_info_ext):
        """Sets the chf_info_ext of this NFProfile.


        :param chf_info_ext: The chf_info_ext of this NFProfile.
        :type chf_info_ext: List[ChfInfo]
        """

        self._chf_info_ext = chf_info_ext

    @property
    def udsf_info(self):
        """Gets the udsf_info of this NFProfile.


        :return: The udsf_info of this NFProfile.
        :rtype: UdsfInfo
        """
        return self._udsf_info

    @udsf_info.setter
    def udsf_info(self, udsf_info):
        """Sets the udsf_info of this NFProfile.


        :param udsf_info: The udsf_info of this NFProfile.
        :type udsf_info: UdsfInfo
        """

        self._udsf_info = udsf_info

    @property
    def udsf_info_ext(self):
        """Gets the udsf_info_ext of this NFProfile.


        :return: The udsf_info_ext of this NFProfile.
        :rtype: List[UdsfInfo]
        """
        return self._udsf_info_ext

    @udsf_info_ext.setter
    def udsf_info_ext(self, udsf_info_ext):
        """Sets the udsf_info_ext of this NFProfile.


        :param udsf_info_ext: The udsf_info_ext of this NFProfile.
        :type udsf_info_ext: List[UdsfInfo]
        """

        self._udsf_info_ext = udsf_info_ext

    @property
    def nwdaf_info(self):
        """Gets the nwdaf_info of this NFProfile.


        :return: The nwdaf_info of this NFProfile.
        :rtype: NwdafInfo
        """
        return self._nwdaf_info

    @nwdaf_info.setter
    def nwdaf_info(self, nwdaf_info):
        """Sets the nwdaf_info of this NFProfile.


        :param nwdaf_info: The nwdaf_info of this NFProfile.
        :type nwdaf_info: NwdafInfo
        """

        self._nwdaf_info = nwdaf_info

    @property
    def nef_info(self):
        """Gets the nef_info of this NFProfile.


        :return: The nef_info of this NFProfile.
        :rtype: NefInfo
        """
        return self._nef_info

    @nef_info.setter
    def nef_info(self, nef_info):
        """Sets the nef_info of this NFProfile.


        :param nef_info: The nef_info of this NFProfile.
        :type nef_info: NefInfo
        """

        self._nef_info = nef_info

    @property
    def pcscf_info(self):
        """Gets the pcscf_info of this NFProfile.


        :return: The pcscf_info of this NFProfile.
        :rtype: List[PcscfInfo]
        """
        return self._pcscf_info

    @pcscf_info.setter
    def pcscf_info(self, pcscf_info):
        """Sets the pcscf_info of this NFProfile.


        :param pcscf_info: The pcscf_info of this NFProfile.
        :type pcscf_info: List[PcscfInfo]
        """

        self._pcscf_info = pcscf_info

    @property
    def hss_info(self):
        """Gets the hss_info of this NFProfile.


        :return: The hss_info of this NFProfile.
        :rtype: List[HssInfo]
        """
        return self._hss_info

    @hss_info.setter
    def hss_info(self, hss_info):
        """Sets the hss_info of this NFProfile.


        :param hss_info: The hss_info of this NFProfile.
        :type hss_info: List[HssInfo]
        """

        self._hss_info = hss_info

    @property
    def custom_info(self):
        """Gets the custom_info of this NFProfile.


        :return: The custom_info of this NFProfile.
        :rtype: object
        """
        return self._custom_info

    @custom_info.setter
    def custom_info(self, custom_info):
        """Sets the custom_info of this NFProfile.


        :param custom_info: The custom_info of this NFProfile.
        :type custom_info: object
        """

        self._custom_info = custom_info

    @property
    def recovery_time(self):
        """Gets the recovery_time of this NFProfile.


        :return: The recovery_time of this NFProfile.
        :rtype: datetime
        """
        return self._recovery_time

    @recovery_time.setter
    def recovery_time(self, recovery_time):
        """Sets the recovery_time of this NFProfile.


        :param recovery_time: The recovery_time of this NFProfile.
        :type recovery_time: datetime
        """

        self._recovery_time = recovery_time

    @property
    def nf_service_persistence(self):
        """Gets the nf_service_persistence of this NFProfile.


        :return: The nf_service_persistence of this NFProfile.
        :rtype: bool
        """
        return self._nf_service_persistence

    @nf_service_persistence.setter
    def nf_service_persistence(self, nf_service_persistence):
        """Sets the nf_service_persistence of this NFProfile.


        :param nf_service_persistence: The nf_service_persistence of this NFProfile.
        :type nf_service_persistence: bool
        """

        self._nf_service_persistence = nf_service_persistence

    @property
    def nf_services(self):
        """Gets the nf_services of this NFProfile.


        :return: The nf_services of this NFProfile.
        :rtype: List[NFService]
        """
        return self._nf_services

    @nf_services.setter
    def nf_services(self, nf_services):
        """Sets the nf_services of this NFProfile.


        :param nf_services: The nf_services of this NFProfile.
        :type nf_services: List[NFService]
        """

        self._nf_services = nf_services

    @property
    def default_notification_subscriptions(self):
        """Gets the default_notification_subscriptions of this NFProfile.


        :return: The default_notification_subscriptions of this NFProfile.
        :rtype: List[DefaultNotificationSubscription]
        """
        return self._default_notification_subscriptions

    @default_notification_subscriptions.setter
    def default_notification_subscriptions(self, default_notification_subscriptions):
        """Sets the default_notification_subscriptions of this NFProfile.


        :param default_notification_subscriptions: The default_notification_subscriptions of this NFProfile.
        :type default_notification_subscriptions: List[DefaultNotificationSubscription]
        """

        self._default_notification_subscriptions = default_notification_subscriptions

    @property
    def lmf_info(self):
        """Gets the lmf_info of this NFProfile.


        :return: The lmf_info of this NFProfile.
        :rtype: LmfInfo
        """
        return self._lmf_info

    @lmf_info.setter
    def lmf_info(self, lmf_info):
        """Sets the lmf_info of this NFProfile.


        :param lmf_info: The lmf_info of this NFProfile.
        :type lmf_info: LmfInfo
        """

        self._lmf_info = lmf_info

    @property
    def gmlc_info(self):
        """Gets the gmlc_info of this NFProfile.


        :return: The gmlc_info of this NFProfile.
        :rtype: GmlcInfo
        """
        return self._gmlc_info

    @gmlc_info.setter
    def gmlc_info(self, gmlc_info):
        """Sets the gmlc_info of this NFProfile.


        :param gmlc_info: The gmlc_info of this NFProfile.
        :type gmlc_info: GmlcInfo
        """

        self._gmlc_info = gmlc_info

    @property
    def snpn_list(self):
        """Gets the snpn_list of this NFProfile.


        :return: The snpn_list of this NFProfile.
        :rtype: List[PlmnIdNid]
        """
        return self._snpn_list

    @snpn_list.setter
    def snpn_list(self, snpn_list):
        """Sets the snpn_list of this NFProfile.


        :param snpn_list: The snpn_list of this NFProfile.
        :type snpn_list: List[PlmnIdNid]
        """

        self._snpn_list = snpn_list

    @property
    def nf_set_id_list(self):
        """Gets the nf_set_id_list of this NFProfile.


        :return: The nf_set_id_list of this NFProfile.
        :rtype: List[str]
        """
        return self._nf_set_id_list

    @nf_set_id_list.setter
    def nf_set_id_list(self, nf_set_id_list):
        """Sets the nf_set_id_list of this NFProfile.


        :param nf_set_id_list: The nf_set_id_list of this NFProfile.
        :type nf_set_id_list: List[str]
        """

        self._nf_set_id_list = nf_set_id_list

    @property
    def serving_scope(self):
        """Gets the serving_scope of this NFProfile.


        :return: The serving_scope of this NFProfile.
        :rtype: List[str]
        """
        return self._serving_scope

    @serving_scope.setter
    def serving_scope(self, serving_scope):
        """Sets the serving_scope of this NFProfile.


        :param serving_scope: The serving_scope of this NFProfile.
        :type serving_scope: List[str]
        """

        self._serving_scope = serving_scope

    @property
    def lc_h_support_ind(self):
        """Gets the lc_h_support_ind of this NFProfile.


        :return: The lc_h_support_ind of this NFProfile.
        :rtype: bool
        """
        return self._lc_h_support_ind

    @lc_h_support_ind.setter
    def lc_h_support_ind(self, lc_h_support_ind):
        """Sets the lc_h_support_ind of this NFProfile.


        :param lc_h_support_ind: The lc_h_support_ind of this NFProfile.
        :type lc_h_support_ind: bool
        """

        self._lc_h_support_ind = lc_h_support_ind

    @property
    def olc_h_support_ind(self):
        """Gets the olc_h_support_ind of this NFProfile.


        :return: The olc_h_support_ind of this NFProfile.
        :rtype: bool
        """
        return self._olc_h_support_ind

    @olc_h_support_ind.setter
    def olc_h_support_ind(self, olc_h_support_ind):
        """Sets the olc_h_support_ind of this NFProfile.


        :param olc_h_support_ind: The olc_h_support_ind of this NFProfile.
        :type olc_h_support_ind: bool
        """

        self._olc_h_support_ind = olc_h_support_ind
