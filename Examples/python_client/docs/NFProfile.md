# NFProfile

Information of an NF Instance discovered by the NRF
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nf_instance_id** | **str** |  | 
**nf_instance_name** | **str** |  | [optional] 
**nf_type** | [**NFType**](NFType.md) |  | 
**nf_status** | [**NFStatus**](NFStatus.md) |  | 
**plmn_list** | [**list[PlmnId]**](PlmnId.md) |  | [optional] 
**s_nssais** | [**list[Snssai]**](Snssai.md) |  | [optional] 
**per_plmn_snssai_list** | [**list[PlmnSnssai]**](PlmnSnssai.md) |  | [optional] 
**nsi_list** | **list[str]** |  | [optional] 
**fqdn** | **str** | Fully Qualified Domain Name | [optional] 
**ipv4_addresses** | **list[str]** |  | [optional] 
**ipv6_addresses** | [**list[Ipv6Addr]**](Ipv6Addr.md) |  | [optional] 
**capacity** | **int** |  | [optional] 
**load** | **int** |  | [optional] 
**load_time_stamp** | **datetime** |  | [optional] 
**locality** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**udr_info** | [**UdrInfo**](UdrInfo.md) |  | [optional] 
**udr_info_ext** | [**list[UdrInfo]**](UdrInfo.md) |  | [optional] 
**udm_info** | [**UdmInfo**](UdmInfo.md) |  | [optional] 
**udm_info_ext** | [**list[UdmInfo]**](UdmInfo.md) |  | [optional] 
**ausf_info** | [**AusfInfo**](AusfInfo.md) |  | [optional] 
**ausf_info_ext** | [**list[AusfInfo]**](AusfInfo.md) |  | [optional] 
**amf_info** | [**AmfInfo**](AmfInfo.md) |  | [optional] 
**amf_info_ext** | [**list[AmfInfo]**](AmfInfo.md) |  | [optional] 
**smf_info** | [**SmfInfo**](SmfInfo.md) |  | [optional] 
**smf_info_ext** | [**list[SmfInfo]**](SmfInfo.md) |  | [optional] 
**upf_info** | [**UpfInfo**](UpfInfo.md) |  | [optional] 
**upf_info_ext** | [**list[UpfInfo]**](UpfInfo.md) |  | [optional] 
**pcf_info** | [**PcfInfo**](PcfInfo.md) |  | [optional] 
**pcf_info_ext** | [**list[PcfInfo]**](PcfInfo.md) |  | [optional] 
**bsf_info** | [**BsfInfo**](BsfInfo.md) |  | [optional] 
**bsf_info_ext** | [**list[BsfInfo]**](BsfInfo.md) |  | [optional] 
**chf_info** | [**ChfInfo**](ChfInfo.md) |  | [optional] 
**chf_info_ext** | [**list[ChfInfo]**](ChfInfo.md) |  | [optional] 
**udsf_info** | [**UdsfInfo**](UdsfInfo.md) |  | [optional] 
**udsf_info_ext** | [**list[UdsfInfo]**](UdsfInfo.md) |  | [optional] 
**nwdaf_info** | [**NwdafInfo**](NwdafInfo.md) |  | [optional] 
**nef_info** | [**NefInfo**](NefInfo.md) |  | [optional] 
**pcscf_info** | [**list[PcscfInfo]**](PcscfInfo.md) |  | [optional] 
**hss_info** | [**list[HssInfo]**](HssInfo.md) |  | [optional] 
**custom_info** | **object** |  | [optional] 
**recovery_time** | **datetime** |  | [optional] 
**nf_service_persistence** | **bool** |  | [optional] [default to False]
**nf_services** | [**list[NFService]**](NFService.md) |  | [optional] 
**default_notification_subscriptions** | [**list[DefaultNotificationSubscription]**](DefaultNotificationSubscription.md) |  | [optional] 
**lmf_info** | [**LmfInfo**](LmfInfo.md) |  | [optional] 
**gmlc_info** | [**GmlcInfo**](GmlcInfo.md) |  | [optional] 
**snpn_list** | [**list[PlmnIdNid]**](PlmnIdNid.md) |  | [optional] 
**nf_set_id_list** | **list[str]** |  | [optional] 
**serving_scope** | **list[str]** |  | [optional] 
**lc_h_support_ind** | **bool** |  | [optional] [default to False]
**olc_h_support_ind** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


