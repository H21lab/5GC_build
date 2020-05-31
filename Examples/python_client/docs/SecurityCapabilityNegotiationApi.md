# openapi_client.SecurityCapabilityNegotiationApi

All URIs are relative to *https://example.com/n32c-handshake/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_exchange_capability**](SecurityCapabilityNegotiationApi.md#post_exchange_capability) | **POST** /exchange-capability | Security Capability Negotiation


# **post_exchange_capability**
> SecNegotiateRspData post_exchange_capability(sec_negotiate_req_data)

Security Capability Negotiation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/n32c-handshake/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://example.com/n32c-handshake/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecurityCapabilityNegotiationApi(api_client)
    sec_negotiate_req_data = openapi_client.SecNegotiateReqData() # SecNegotiateReqData | Custom operation for security capability negotiation

    try:
        # Security Capability Negotiation
        api_response = api_instance.post_exchange_capability(sec_negotiate_req_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityCapabilityNegotiationApi->post_exchange_capability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_negotiate_req_data** | [**SecNegotiateReqData**](SecNegotiateReqData.md)| Custom operation for security capability negotiation | 

### Return type

[**SecNegotiateRspData**](SecNegotiateRspData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (Successful negitiation of security capabilities) |  -  |
**400** | Bad request |  -  |
**411** | Length Required |  -  |
**413** | Payload Too Large |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

