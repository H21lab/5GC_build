# openapi_client.N32FContextTerminateApi

All URIs are relative to *https://example.com/n32c-handshake/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_n32f_terminate**](N32FContextTerminateApi.md#post_n32f_terminate) | **POST** /n32f-terminate | N32-f Context Terminate


# **post_n32f_terminate**
> N32fContextInfo post_n32f_terminate(n32f_context_info)

N32-f Context Terminate

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
    api_instance = openapi_client.N32FContextTerminateApi(api_client)
    n32f_context_info = openapi_client.N32fContextInfo() # N32fContextInfo | Custom operation for n32-f context termination

    try:
        # N32-f Context Terminate
        api_response = api_instance.post_n32f_terminate(n32f_context_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling N32FContextTerminateApi->post_n32f_terminate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n32f_context_info** | [**N32fContextInfo**](N32fContextInfo.md)| Custom operation for n32-f context termination | 

### Return type

[**N32fContextInfo**](N32fContextInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (Successful exchange of parameters) |  -  |
**400** | Bad request |  -  |
**411** | Length Required |  -  |
**413** | Payload Too Large |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

