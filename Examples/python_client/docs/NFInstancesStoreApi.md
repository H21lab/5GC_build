# openapi_client.NFInstancesStoreApi

All URIs are relative to *https://example.com/nnrf-disc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_nf_instances**](NFInstancesStoreApi.md#search_nf_instances) | **GET** /nf-instances | Search a collection of NF Instances


# **search_nf_instances**
> SearchResult search_nf_instances(target_nf_type, requester_nf_type, accept_encoding=accept_encoding, requester_nf_instance_id=requester_nf_instance_id, service_names=service_names, requester_nf_instance_fqdn=requester_nf_instance_fqdn, target_plmn_list=target_plmn_list, requester_plmn_list=requester_plmn_list, target_nf_instance_id=target_nf_instance_id, target_nf_fqdn=target_nf_fqdn, hnrf_uri=hnrf_uri, snssais=snssais, requester_snssais=requester_snssais, plmn_specific_snssai_list=plmn_specific_snssai_list, dnn=dnn, nsi_list=nsi_list, smf_serving_area=smf_serving_area, tai=tai, amf_region_id=amf_region_id, amf_set_id=amf_set_id, guami=guami, supi=supi, ue_ipv4_address=ue_ipv4_address, ip_domain=ip_domain, ue_ipv6_prefix=ue_ipv6_prefix, pgw_ind=pgw_ind, pgw=pgw, gpsi=gpsi, external_group_identity=external_group_identity, internal_group_identity=internal_group_identity, pfd_data=pfd_data, data_set=data_set, routing_indicator=routing_indicator, group_id_list=group_id_list, dnai_list=dnai_list, pdu_session_types=pdu_session_types, event_id_list=event_id_list, nwdaf_event_list=nwdaf_event_list, supported_features=supported_features, upf_iwk_eps_ind=upf_iwk_eps_ind, chf_supported_plmn=chf_supported_plmn, preferred_locality=preferred_locality, access_type=access_type, limit=limit, required_features=required_features, complex_query=complex_query, max_payload_size=max_payload_size, atsss_capability=atsss_capability, upf_ue_ip_addr_ind=upf_ue_ip_addr_ind, client_type=client_type, lmf_id=lmf_id, an_node_type=an_node_type, rat_type=rat_type, preferred_tai=preferred_tai, preferred_nf_instances=preferred_nf_instances, if_none_match=if_none_match, target_snpn=target_snpn, af_ee_data=af_ee_data, w_agf_info=w_agf_info, tngf_info=tngf_info, twif_info=twif_info, target_nf_set_id=target_nf_set_id, target_nf_service_set_id=target_nf_service_set_id, nef_id=nef_id, notification_type=notification_type, serving_scope=serving_scope, imsi=imsi, preferred_api_versions=preferred_api_versions, v2x_support_ind=v2x_support_ind, redundant_gtpu=redundant_gtpu, redundant_transport=redundant_transport)

Search a collection of NF Instances

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/nnrf-disc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.com/nnrf-disc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials
configuration = openapi_client.Configuration(
    host = "https://example.com/nnrf-disc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NFInstancesStoreApi(api_client)
    target_nf_type = openapi_client.NFType() # NFType | Type of the target NF
requester_nf_type = openapi_client.NFType() # NFType | Type of the requester NF
accept_encoding = 'accept_encoding_example' # str | Accept-Encoding, described in IETF RFC 7231 (optional)
requester_nf_instance_id = 'requester_nf_instance_id_example' # str | NfInstanceId of the requester NF (optional)
service_names = [openapi_client.ServiceName()] # list[ServiceName] | Names of the services offered by the NF (optional)
requester_nf_instance_fqdn = 'requester_nf_instance_fqdn_example' # str | FQDN of the requester NF (optional)
target_plmn_list = [openapi_client.PlmnId()] # list[PlmnId] | Id of the PLMN of the target NF (optional)
requester_plmn_list = [openapi_client.PlmnId()] # list[PlmnId] | Id of the PLMN where the NF issuing the Discovery request is located (optional)
target_nf_instance_id = 'target_nf_instance_id_example' # str | Identity of the NF instance being discovered (optional)
target_nf_fqdn = 'target_nf_fqdn_example' # str | FQDN of the NF instance being discovered (optional)
hnrf_uri = 'hnrf_uri_example' # str | Uri of the home NRF (optional)
snssais = [openapi_client.Snssai()] # list[Snssai] | Slice info of the target NF (optional)
requester_snssais = [openapi_client.Snssai()] # list[Snssai] | Slice info of the requester NF (optional)
plmn_specific_snssai_list = [openapi_client.PlmnSnssai()] # list[PlmnSnssai] | PLMN specific Slice info of the target NF (optional)
dnn = 'dnn_example' # str | Dnn supported by the BSF, SMF or UPF (optional)
nsi_list = ['nsi_list_example'] # list[str] | NSI IDs that are served by the services being discovered (optional)
smf_serving_area = 'smf_serving_area_example' # str |  (optional)
tai = openapi_client.Tai() # Tai | Tracking Area Identity (optional)
amf_region_id = 'amf_region_id_example' # str | AMF Region Identity (optional)
amf_set_id = 'amf_set_id_example' # str | AMF Set Identity (optional)
guami = openapi_client.Guami() # Guami | Guami used to search for an appropriate AMF (optional)
supi = 'supi_example' # str | SUPI of the user (optional)
ue_ipv4_address = 'ue_ipv4_address_example' # str | IPv4 address of the UE (optional)
ip_domain = 'ip_domain_example' # str | IP domain of the UE, which supported by BSF (optional)
ue_ipv6_prefix = openapi_client.Ipv6Prefix() # Ipv6Prefix | IPv6 prefix of the UE (optional)
pgw_ind = True # bool | Combined PGW-C and SMF or a standalone SMF (optional)
pgw = 'pgw_example' # str | PGW FQDN of a combined PGW-C and SMF (optional)
gpsi = 'gpsi_example' # str | GPSI of the user (optional)
external_group_identity = 'external_group_identity_example' # str | external group identifier of the user (optional)
internal_group_identity = 'internal_group_identity_example' # str | internal group identifier of the user (optional)
pfd_data = openapi_client.PfdData() # PfdData | PFD data (optional)
data_set = openapi_client.DataSetId() # DataSetId | data set supported by the NF (optional)
routing_indicator = 'routing_indicator_example' # str | routing indicator in SUCI (optional)
group_id_list = ['group_id_list_example'] # list[str] | Group IDs of the NFs being discovered (optional)
dnai_list = ['dnai_list_example'] # list[str] | Data network access identifiers of the NFs being discovered (optional)
pdu_session_types = [openapi_client.PduSessionType()] # list[PduSessionType] | list of PDU Session Type required to be supported by the target NF (optional)
event_id_list = [openapi_client.EventId()] # list[EventId] | Analytics event(s) requested to be supported by the Nnwdaf_AnalyticsInfo service (optional)
nwdaf_event_list = [openapi_client.NwdafEvent()] # list[NwdafEvent] | Analytics event(s) requested to be supported by the Nnwdaf_EventsSubscription service. (optional)
supported_features = 'supported_features_example' # str | Features required to be supported by the target NF (optional)
upf_iwk_eps_ind = True # bool | UPF supporting interworking with EPS or not (optional)
chf_supported_plmn = openapi_client.PlmnId() # PlmnId | PLMN ID supported by a CHF (optional)
preferred_locality = 'preferred_locality_example' # str | preferred target NF location (optional)
access_type = openapi_client.AccessType() # AccessType | AccessType supported by the target NF (optional)
limit = 56 # int | Maximum number of NFProfiles to return in the response (optional)
required_features = ['required_features_example'] # list[str] | Features required to be supported by the target NF (optional)
complex_query = openapi_client.ComplexQuery() # ComplexQuery | the complex query condition expression (optional)
max_payload_size = 124 # int | Maximum payload size of the response expressed in kilo octets (optional) (default to 124)
atsss_capability = openapi_client.AtsssCapability() # AtsssCapability | ATSSS Capability (optional)
upf_ue_ip_addr_ind = True # bool | UPF supporting allocating UE IP addresses/prefixes (optional)
client_type = openapi_client.ExternalClientType() # ExternalClientType | Requested client type served by the NF (optional)
lmf_id = 'lmf_id_example' # str | LMF identification to be discovered (optional)
an_node_type = openapi_client.AnNodeType() # AnNodeType | Requested AN node type served by the NF (optional)
rat_type = openapi_client.RatType() # RatType | Requested RAT type served by the NF (optional)
preferred_tai = openapi_client.Tai() # Tai | preferred Tracking Area Identity (optional)
preferred_nf_instances = ['preferred_nf_instances_example'] # list[str] | preferred NF Instances (optional)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests, as described in IETF RFC 7232, 3.2 (optional)
target_snpn = openapi_client.PlmnIdNid() # PlmnIdNid | Target SNPN Identity (optional)
af_ee_data = openapi_client.AfEventExposureData() # AfEventExposureData | NEF exposured by the AF (optional)
w_agf_info = openapi_client.WAgfInfo() # WAgfInfo | UPF collocated with W-AGF (optional)
tngf_info = openapi_client.TngfInfo() # TngfInfo | UPF collocated with TNGF (optional)
twif_info = openapi_client.TwifInfo() # TwifInfo | UPF collocated with TWIF (optional)
target_nf_set_id = 'target_nf_set_id_example' # str | Target NF Set ID (optional)
target_nf_service_set_id = 'target_nf_service_set_id_example' # str | Target NF Service Set ID (optional)
nef_id = 'nef_id_example' # str | NEF ID (optional)
notification_type = openapi_client.NotificationType() # NotificationType | Notification Type (optional)
serving_scope = ['serving_scope_example'] # list[str] | areas that can be served by the target NF (optional)
imsi = 'imsi_example' # str | IMSI of the requester UE to search for an appropriate NF (e.g. HSS) (optional)
preferred_api_versions = {'key': 'preferred_api_versions_example'} # dict(str, str) | Preferred API version of the services to be discovered (optional)
v2x_support_ind = True # bool | PCF supports V2X (optional)
redundant_gtpu = True # bool | UPF supports redundant gtp-u to be discovered (optional)
redundant_transport = True # bool | UPF supports redundant transport path to be discovered (optional)

    try:
        # Search a collection of NF Instances
        api_response = api_instance.search_nf_instances(target_nf_type, requester_nf_type, accept_encoding=accept_encoding, requester_nf_instance_id=requester_nf_instance_id, service_names=service_names, requester_nf_instance_fqdn=requester_nf_instance_fqdn, target_plmn_list=target_plmn_list, requester_plmn_list=requester_plmn_list, target_nf_instance_id=target_nf_instance_id, target_nf_fqdn=target_nf_fqdn, hnrf_uri=hnrf_uri, snssais=snssais, requester_snssais=requester_snssais, plmn_specific_snssai_list=plmn_specific_snssai_list, dnn=dnn, nsi_list=nsi_list, smf_serving_area=smf_serving_area, tai=tai, amf_region_id=amf_region_id, amf_set_id=amf_set_id, guami=guami, supi=supi, ue_ipv4_address=ue_ipv4_address, ip_domain=ip_domain, ue_ipv6_prefix=ue_ipv6_prefix, pgw_ind=pgw_ind, pgw=pgw, gpsi=gpsi, external_group_identity=external_group_identity, internal_group_identity=internal_group_identity, pfd_data=pfd_data, data_set=data_set, routing_indicator=routing_indicator, group_id_list=group_id_list, dnai_list=dnai_list, pdu_session_types=pdu_session_types, event_id_list=event_id_list, nwdaf_event_list=nwdaf_event_list, supported_features=supported_features, upf_iwk_eps_ind=upf_iwk_eps_ind, chf_supported_plmn=chf_supported_plmn, preferred_locality=preferred_locality, access_type=access_type, limit=limit, required_features=required_features, complex_query=complex_query, max_payload_size=max_payload_size, atsss_capability=atsss_capability, upf_ue_ip_addr_ind=upf_ue_ip_addr_ind, client_type=client_type, lmf_id=lmf_id, an_node_type=an_node_type, rat_type=rat_type, preferred_tai=preferred_tai, preferred_nf_instances=preferred_nf_instances, if_none_match=if_none_match, target_snpn=target_snpn, af_ee_data=af_ee_data, w_agf_info=w_agf_info, tngf_info=tngf_info, twif_info=twif_info, target_nf_set_id=target_nf_set_id, target_nf_service_set_id=target_nf_service_set_id, nef_id=nef_id, notification_type=notification_type, serving_scope=serving_scope, imsi=imsi, preferred_api_versions=preferred_api_versions, v2x_support_ind=v2x_support_ind, redundant_gtpu=redundant_gtpu, redundant_transport=redundant_transport)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NFInstancesStoreApi->search_nf_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_nf_type** | [**NFType**](.md)| Type of the target NF | 
 **requester_nf_type** | [**NFType**](.md)| Type of the requester NF | 
 **accept_encoding** | **str**| Accept-Encoding, described in IETF RFC 7231 | [optional] 
 **requester_nf_instance_id** | [**str**](.md)| NfInstanceId of the requester NF | [optional] 
 **service_names** | [**list[ServiceName]**](ServiceName.md)| Names of the services offered by the NF | [optional] 
 **requester_nf_instance_fqdn** | **str**| FQDN of the requester NF | [optional] 
 **target_plmn_list** | [**list[PlmnId]**](PlmnId.md)| Id of the PLMN of the target NF | [optional] 
 **requester_plmn_list** | [**list[PlmnId]**](PlmnId.md)| Id of the PLMN where the NF issuing the Discovery request is located | [optional] 
 **target_nf_instance_id** | [**str**](.md)| Identity of the NF instance being discovered | [optional] 
 **target_nf_fqdn** | **str**| FQDN of the NF instance being discovered | [optional] 
 **hnrf_uri** | **str**| Uri of the home NRF | [optional] 
 **snssais** | [**list[Snssai]**](Snssai.md)| Slice info of the target NF | [optional] 
 **requester_snssais** | [**list[Snssai]**](Snssai.md)| Slice info of the requester NF | [optional] 
 **plmn_specific_snssai_list** | [**list[PlmnSnssai]**](PlmnSnssai.md)| PLMN specific Slice info of the target NF | [optional] 
 **dnn** | **str**| Dnn supported by the BSF, SMF or UPF | [optional] 
 **nsi_list** | [**list[str]**](str.md)| NSI IDs that are served by the services being discovered | [optional] 
 **smf_serving_area** | **str**|  | [optional] 
 **tai** | [**Tai**](.md)| Tracking Area Identity | [optional] 
 **amf_region_id** | **str**| AMF Region Identity | [optional] 
 **amf_set_id** | **str**| AMF Set Identity | [optional] 
 **guami** | [**Guami**](.md)| Guami used to search for an appropriate AMF | [optional] 
 **supi** | **str**| SUPI of the user | [optional] 
 **ue_ipv4_address** | **str**| IPv4 address of the UE | [optional] 
 **ip_domain** | **str**| IP domain of the UE, which supported by BSF | [optional] 
 **ue_ipv6_prefix** | [**Ipv6Prefix**](.md)| IPv6 prefix of the UE | [optional] 
 **pgw_ind** | **bool**| Combined PGW-C and SMF or a standalone SMF | [optional] 
 **pgw** | **str**| PGW FQDN of a combined PGW-C and SMF | [optional] 
 **gpsi** | **str**| GPSI of the user | [optional] 
 **external_group_identity** | **str**| external group identifier of the user | [optional] 
 **internal_group_identity** | **str**| internal group identifier of the user | [optional] 
 **pfd_data** | [**PfdData**](.md)| PFD data | [optional] 
 **data_set** | [**DataSetId**](.md)| data set supported by the NF | [optional] 
 **routing_indicator** | **str**| routing indicator in SUCI | [optional] 
 **group_id_list** | [**list[str]**](str.md)| Group IDs of the NFs being discovered | [optional] 
 **dnai_list** | [**list[str]**](str.md)| Data network access identifiers of the NFs being discovered | [optional] 
 **pdu_session_types** | [**list[PduSessionType]**](PduSessionType.md)| list of PDU Session Type required to be supported by the target NF | [optional] 
 **event_id_list** | [**list[EventId]**](EventId.md)| Analytics event(s) requested to be supported by the Nnwdaf_AnalyticsInfo service | [optional] 
 **nwdaf_event_list** | [**list[NwdafEvent]**](NwdafEvent.md)| Analytics event(s) requested to be supported by the Nnwdaf_EventsSubscription service. | [optional] 
 **supported_features** | **str**| Features required to be supported by the target NF | [optional] 
 **upf_iwk_eps_ind** | **bool**| UPF supporting interworking with EPS or not | [optional] 
 **chf_supported_plmn** | [**PlmnId**](.md)| PLMN ID supported by a CHF | [optional] 
 **preferred_locality** | **str**| preferred target NF location | [optional] 
 **access_type** | [**AccessType**](.md)| AccessType supported by the target NF | [optional] 
 **limit** | **int**| Maximum number of NFProfiles to return in the response | [optional] 
 **required_features** | [**list[str]**](str.md)| Features required to be supported by the target NF | [optional] 
 **complex_query** | [**ComplexQuery**](.md)| the complex query condition expression | [optional] 
 **max_payload_size** | **int**| Maximum payload size of the response expressed in kilo octets | [optional] [default to 124]
 **atsss_capability** | [**AtsssCapability**](.md)| ATSSS Capability | [optional] 
 **upf_ue_ip_addr_ind** | **bool**| UPF supporting allocating UE IP addresses/prefixes | [optional] 
 **client_type** | [**ExternalClientType**](.md)| Requested client type served by the NF | [optional] 
 **lmf_id** | **str**| LMF identification to be discovered | [optional] 
 **an_node_type** | [**AnNodeType**](.md)| Requested AN node type served by the NF | [optional] 
 **rat_type** | [**RatType**](.md)| Requested RAT type served by the NF | [optional] 
 **preferred_tai** | [**Tai**](.md)| preferred Tracking Area Identity | [optional] 
 **preferred_nf_instances** | [**list[str]**](str.md)| preferred NF Instances | [optional] 
 **if_none_match** | **str**| Validator for conditional requests, as described in IETF RFC 7232, 3.2 | [optional] 
 **target_snpn** | [**PlmnIdNid**](.md)| Target SNPN Identity | [optional] 
 **af_ee_data** | [**AfEventExposureData**](.md)| NEF exposured by the AF | [optional] 
 **w_agf_info** | [**WAgfInfo**](.md)| UPF collocated with W-AGF | [optional] 
 **tngf_info** | [**TngfInfo**](.md)| UPF collocated with TNGF | [optional] 
 **twif_info** | [**TwifInfo**](.md)| UPF collocated with TWIF | [optional] 
 **target_nf_set_id** | **str**| Target NF Set ID | [optional] 
 **target_nf_service_set_id** | **str**| Target NF Service Set ID | [optional] 
 **nef_id** | **str**| NEF ID | [optional] 
 **notification_type** | [**NotificationType**](.md)| Notification Type | [optional] 
 **serving_scope** | [**list[str]**](str.md)| areas that can be served by the target NF | [optional] 
 **imsi** | **str**| IMSI of the requester UE to search for an appropriate NF (e.g. HSS) | [optional] 
 **preferred_api_versions** | [**dict(str, str)**](str.md)| Preferred API version of the services to be discovered | [optional] 
 **v2x_support_ind** | **bool**| PCF supports V2X | [optional] 
 **redundant_gtpu** | **bool**| UPF supports redundant gtp-u to be discovered | [optional] 
 **redundant_transport** | **bool**| UPF supports redundant transport path to be discovered | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  * Cache-Control - Cache-Control containing max-age, described in IETF RFC 7234, 5.2 <br>  * ETag - Entity Tag containing a strong validator, described in IETF RFC 7232, 2.3 <br>  * Content-Encoding - Content-Encoding, described in IETF RFC 7231 <br>  |
**307** | Temporary Redirect |  * Location - The URI pointing to the resource located on the redirect target NRF <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | 406 Not Acceptable |  -  |
**411** | Length Required |  -  |
**413** | Payload Too Large |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**503** | Service Unavailable |  -  |
**0** | Generic Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

