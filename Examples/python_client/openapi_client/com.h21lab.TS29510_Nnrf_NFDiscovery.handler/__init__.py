# coding: utf-8

# flake8: noqa
"""
    NRF NFDiscovery Service

    NRF NFDiscovery Service. © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.   # noqa: E501

    The version of the OpenAPI document: 1.1.0.alpha-4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.access_type import AccessType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.af_event import AfEvent
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.af_event_exposure_data import AfEventExposureData
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.amf_info import AmfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.an_node_type import AnNodeType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atom import Atom
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atsss_capability import AtsssCapability
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ausf_info import AusfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.bsf_info import BsfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.chf_info import ChfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.chf_service_info import ChfServiceInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf import Cnf
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf_unit import CnfUnit
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.complex_query import ComplexQuery
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.data_set_id import DataSetId
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.default_notification_subscription import DefaultNotificationSubscription
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf import Dnf
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf_unit import DnfUnit
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnn_smf_info_item import DnnSmfInfoItem
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnn_upf_info_item import DnnUpfInfoItem
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.event_id import EventId
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.external_client_type import ExternalClientType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.gmlc_info import GmlcInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.guami import Guami
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.hss_info import HssInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.identity_range import IdentityRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.imsi_range import ImsiRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.interface_upf_info_item import InterfaceUpfInfoItem
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.internal_group_id_range import InternalGroupIdRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.invalid_param import InvalidParam
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ip_end_point import IpEndPoint
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv4_address_range import Ipv4AddressRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_addr import Ipv6Addr
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_prefix import Ipv6Prefix
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_prefix_range import Ipv6PrefixRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.lmf_info import LmfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.n1_message_class import N1MessageClass
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.n2_information_class import N2InformationClass
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.n2_interface_amf_info import N2InterfaceAmfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_profile import NFProfile
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_service import NFService
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_service_status import NFServiceStatus
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_service_version import NFServiceVersion
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_status import NFStatus
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_type import NFType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nef_info import NefInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.notification_type import NotificationType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nwdaf_event import NwdafEvent
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nwdaf_info import NwdafInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcf_info import PcfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcscf_info import PcscfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pdu_session_type import PduSessionType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pfd_data import PfdData
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id import PlmnId
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id_nid import PlmnIdNid
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_range import PlmnRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_snssai import PlmnSnssai
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.preferred_search import PreferredSearch
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.problem_details import ProblemDetails
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.rat_type import RatType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.search_result import SearchResult
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.service_name import ServiceName
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.smf_info import SmfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai import Snssai
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai_smf_info_item import SnssaiSmfInfoItem
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai_upf_info_item import SnssaiUpfInfoItem
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.stored_search_result import StoredSearchResult
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.supi_range import SupiRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tac_range import TacRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai_range import TaiRange
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tngf_info import TngfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.transport_protocol import TransportProtocol
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.twif_info import TwifInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.up_interface_type import UPInterfaceType
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udm_info import UdmInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udr_info import UdrInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.udsf_info import UdsfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.upf_info import UpfInfo
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.uri_scheme import UriScheme
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.vendor_specific_feature import VendorSpecificFeature
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.w_agf_info import WAgfInfo
