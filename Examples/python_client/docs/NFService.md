# NFService

Information of a given NF Service Instance; it is part of the NFProfile of an NF Instance discovered by the NRF
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_instance_id** | **str** |  | 
**service_name** | [**ServiceName**](ServiceName.md) |  | 
**versions** | [**list[NFServiceVersion]**](NFServiceVersion.md) |  | 
**scheme** | [**UriScheme**](UriScheme.md) |  | 
**nf_service_status** | [**NFServiceStatus**](NFServiceStatus.md) |  | 
**fqdn** | **str** | Fully Qualified Domain Name | [optional] 
**ip_end_points** | [**list[IpEndPoint]**](IpEndPoint.md) |  | [optional] 
**api_prefix** | **str** |  | [optional] 
**default_notification_subscriptions** | [**list[DefaultNotificationSubscription]**](DefaultNotificationSubscription.md) |  | [optional] 
**capacity** | **int** |  | [optional] 
**load** | **int** |  | [optional] 
**load_time_stamp** | **datetime** |  | [optional] 
**priority** | **int** |  | [optional] 
**recovery_time** | **datetime** |  | [optional] 
**chf_service_info** | [**ChfServiceInfo**](ChfServiceInfo.md) |  | [optional] 
**supported_features** | **str** |  | [optional] 
**nf_service_set_id_list** | **list[str]** |  | [optional] 
**s_nssais** | [**list[Snssai]**](Snssai.md) |  | [optional] 
**per_plmn_snssai_list** | [**list[PlmnSnssai]**](PlmnSnssai.md) |  | [optional] 
**vendor_id** | **str** | Vendor ID of the NF Service instance (Private Enterprise Number assigned by IANA) | [optional] 
**supported_vendor_specific_features** | **dict(str, list[VendorSpecificFeature])** |  | [optional] 
**oauth2_required** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


