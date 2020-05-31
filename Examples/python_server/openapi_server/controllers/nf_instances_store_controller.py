import connexion
import six

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.access_type import AccessType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.af_event_exposure_data import AfEventExposureData  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.an_node_type import AnNodeType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atsss_capability import AtsssCapability  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.complex_query import ComplexQuery  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.data_set_id import DataSetId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.event_id import EventId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.external_client_type import ExternalClientType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.guami import Guami  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_prefix import Ipv6Prefix  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_type import NFType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.notification_type import NotificationType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nwdaf_event import NwdafEvent  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pdu_session_type import PduSessionType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pfd_data import PfdData  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id import PlmnId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id_nid import PlmnIdNid  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_snssai import PlmnSnssai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.rat_type import RatType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.search_result import SearchResult  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.service_name import ServiceName  # noqa: E501
java.util.*  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai import Snssai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tngf_info import TngfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.twif_info import TwifInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.w_agf_info import WAgfInfo  # noqa: E501
from openapi_server import util


def search_nf_instances(target_nf_type, requester_nf_type, accept_encoding=None, requester_nf_instance_id=None, service_names=None, requester_nf_instance_fqdn=None, target_plmn_list=None, requester_plmn_list=None, target_nf_instance_id=None, target_nf_fqdn=None, hnrf_uri=None, snssais=None, requester_snssais=None, plmn_specific_snssai_list=None, dnn=None, nsi_list=None, smf_serving_area=None, tai=None, amf_region_id=None, amf_set_id=None, guami=None, supi=None, ue_ipv4_address=None, ip_domain=None, ue_ipv6_prefix=None, pgw_ind=None, pgw=None, gpsi=None, external_group_identity=None, internal_group_identity=None, pfd_data=None, data_set=None, routing_indicator=None, group_id_list=None, dnai_list=None, pdu_session_types=None, event_id_list=None, nwdaf_event_list=None, supported_features=None, upf_iwk_eps_ind=None, chf_supported_plmn=None, preferred_locality=None, access_type=None, limit=None, required_features=None, complex_query=None, max_payload_size=None, atsss_capability=None, upf_ue_ip_addr_ind=None, client_type=None, lmf_id=None, an_node_type=None, rat_type=None, preferred_tai=None, preferred_nf_instances=None, if_none_match=None, target_snpn=None, af_ee_data=None, w_agf_info=None, tngf_info=None, twif_info=None, target_nf_set_id=None, target_nf_service_set_id=None, nef_id=None, notification_type=None, serving_scope=None, imsi=None, preferred_api_versions=None, v2x_support_ind=None, redundant_gtpu=None, redundant_transport=None):  # noqa: E501
    """Search a collection of NF Instances

     # noqa: E501

    :param target_nf_type: Type of the target NF
    :type target_nf_type: dict | bytes
    :param requester_nf_type: Type of the requester NF
    :type requester_nf_type: dict | bytes
    :param accept_encoding: Accept-Encoding, described in IETF RFC 7231
    :type accept_encoding: str
    :param requester_nf_instance_id: NfInstanceId of the requester NF
    :type requester_nf_instance_id: 
    :param service_names: Names of the services offered by the NF
    :type service_names: list | bytes
    :param requester_nf_instance_fqdn: FQDN of the requester NF
    :type requester_nf_instance_fqdn: str
    :param target_plmn_list: Id of the PLMN of the target NF
    :type target_plmn_list: list | bytes
    :param requester_plmn_list: Id of the PLMN where the NF issuing the Discovery request is located
    :type requester_plmn_list: list | bytes
    :param target_nf_instance_id: Identity of the NF instance being discovered
    :type target_nf_instance_id: 
    :param target_nf_fqdn: FQDN of the NF instance being discovered
    :type target_nf_fqdn: str
    :param hnrf_uri: Uri of the home NRF
    :type hnrf_uri: str
    :param snssais: Slice info of the target NF
    :type snssais: list | bytes
    :param requester_snssais: Slice info of the requester NF
    :type requester_snssais: list | bytes
    :param plmn_specific_snssai_list: PLMN specific Slice info of the target NF
    :type plmn_specific_snssai_list: list | bytes
    :param dnn: Dnn supported by the BSF, SMF or UPF
    :type dnn: str
    :param nsi_list: NSI IDs that are served by the services being discovered
    :type nsi_list: List[str]
    :param smf_serving_area: 
    :type smf_serving_area: str
    :param tai: Tracking Area Identity
    :type tai: dict | bytes
    :param amf_region_id: AMF Region Identity
    :type amf_region_id: str
    :param amf_set_id: AMF Set Identity
    :type amf_set_id: str
    :param guami: Guami used to search for an appropriate AMF
    :type guami: dict | bytes
    :param supi: SUPI of the user
    :type supi: str
    :param ue_ipv4_address: IPv4 address of the UE
    :type ue_ipv4_address: str
    :param ip_domain: IP domain of the UE, which supported by BSF
    :type ip_domain: str
    :param ue_ipv6_prefix: IPv6 prefix of the UE
    :type ue_ipv6_prefix: dict | bytes
    :param pgw_ind: Combined PGW-C and SMF or a standalone SMF
    :type pgw_ind: bool
    :param pgw: PGW FQDN of a combined PGW-C and SMF
    :type pgw: str
    :param gpsi: GPSI of the user
    :type gpsi: str
    :param external_group_identity: external group identifier of the user
    :type external_group_identity: str
    :param internal_group_identity: internal group identifier of the user
    :type internal_group_identity: str
    :param pfd_data: PFD data
    :type pfd_data: dict | bytes
    :param data_set: data set supported by the NF
    :type data_set: dict | bytes
    :param routing_indicator: routing indicator in SUCI
    :type routing_indicator: str
    :param group_id_list: Group IDs of the NFs being discovered
    :type group_id_list: List[str]
    :param dnai_list: Data network access identifiers of the NFs being discovered
    :type dnai_list: List[str]
    :param pdu_session_types: list of PDU Session Type required to be supported by the target NF
    :type pdu_session_types: list | bytes
    :param event_id_list: Analytics event(s) requested to be supported by the Nnwdaf_AnalyticsInfo service
    :type event_id_list: list | bytes
    :param nwdaf_event_list: Analytics event(s) requested to be supported by the Nnwdaf_EventsSubscription service.
    :type nwdaf_event_list: list | bytes
    :param supported_features: Features required to be supported by the target NF
    :type supported_features: str
    :param upf_iwk_eps_ind: UPF supporting interworking with EPS or not
    :type upf_iwk_eps_ind: bool
    :param chf_supported_plmn: PLMN ID supported by a CHF
    :type chf_supported_plmn: dict | bytes
    :param preferred_locality: preferred target NF location
    :type preferred_locality: str
    :param access_type: AccessType supported by the target NF
    :type access_type: dict | bytes
    :param limit: Maximum number of NFProfiles to return in the response
    :type limit: int
    :param required_features: Features required to be supported by the target NF
    :type required_features: List[str]
    :param complex_query: the complex query condition expression
    :type complex_query: dict | bytes
    :param max_payload_size: Maximum payload size of the response expressed in kilo octets
    :type max_payload_size: int
    :param atsss_capability: ATSSS Capability
    :type atsss_capability: dict | bytes
    :param upf_ue_ip_addr_ind: UPF supporting allocating UE IP addresses/prefixes
    :type upf_ue_ip_addr_ind: bool
    :param client_type: Requested client type served by the NF
    :type client_type: dict | bytes
    :param lmf_id: LMF identification to be discovered
    :type lmf_id: str
    :param an_node_type: Requested AN node type served by the NF
    :type an_node_type: dict | bytes
    :param rat_type: Requested RAT type served by the NF
    :type rat_type: dict | bytes
    :param preferred_tai: preferred Tracking Area Identity
    :type preferred_tai: dict | bytes
    :param preferred_nf_instances: preferred NF Instances
    :type preferred_nf_instances: List[str]
    :param if_none_match: Validator for conditional requests, as described in IETF RFC 7232, 3.2
    :type if_none_match: str
    :param target_snpn: Target SNPN Identity
    :type target_snpn: dict | bytes
    :param af_ee_data: NEF exposured by the AF
    :type af_ee_data: dict | bytes
    :param w_agf_info: UPF collocated with W-AGF
    :type w_agf_info: dict | bytes
    :param tngf_info: UPF collocated with TNGF
    :type tngf_info: dict | bytes
    :param twif_info: UPF collocated with TWIF
    :type twif_info: dict | bytes
    :param target_nf_set_id: Target NF Set ID
    :type target_nf_set_id: str
    :param target_nf_service_set_id: Target NF Service Set ID
    :type target_nf_service_set_id: str
    :param nef_id: NEF ID
    :type nef_id: str
    :param notification_type: Notification Type
    :type notification_type: dict | bytes
    :param serving_scope: areas that can be served by the target NF
    :type serving_scope: List[str]
    :param imsi: IMSI of the requester UE to search for an appropriate NF (e.g. HSS)
    :type imsi: str
    :param preferred_api_versions: Preferred API version of the services to be discovered
    :type preferred_api_versions: Dict[str, str]
    :param v2x_support_ind: PCF supports V2X
    :type v2x_support_ind: bool
    :param redundant_gtpu: UPF supports redundant gtp-u to be discovered
    :type redundant_gtpu: bool
    :param redundant_transport: UPF supports redundant transport path to be discovered
    :type redundant_transport: bool

    :rtype: SearchResult
    """
    if connexion.request.is_json:
        target_nf_type =  NFType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        requester_nf_type =  NFType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        service_names = [ServiceName.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        target_plmn_list = [PlmnId.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        requester_plmn_list = [PlmnId.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        snssais = [Snssai.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        requester_snssais = [Snssai.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        plmn_specific_snssai_list = [PlmnSnssai.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        tai =  Tai.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        guami =  Guami.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        ue_ipv6_prefix =  Ipv6Prefix.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        pfd_data =  PfdData.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data_set =  DataSetId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        pdu_session_types = [PduSessionType.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        event_id_list = [EventId.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        nwdaf_event_list = [NwdafEvent.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        chf_supported_plmn =  PlmnId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        access_type =  AccessType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        complex_query =  ComplexQuery.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        atsss_capability =  AtsssCapability.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        client_type =  ExternalClientType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        an_node_type =  AnNodeType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        rat_type =  RatType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        preferred_tai =  Tai.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        target_snpn =  PlmnIdNid.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        af_ee_data =  AfEventExposureData.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        w_agf_info =  WAgfInfo.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        tngf_info =  TngfInfo.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        twif_info =  TwifInfo.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        notification_type =  NotificationType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
