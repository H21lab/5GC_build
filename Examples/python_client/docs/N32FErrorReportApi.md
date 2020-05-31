# openapi_client.N32FErrorReportApi

All URIs are relative to *https://example.com/n32c-handshake/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_n32f_error**](N32FErrorReportApi.md#post_n32f_error) | **POST** /n32f-error | N32-f Error Reporting Procedure


# **post_n32f_error**
> post_n32f_error(n32f_error_info)

N32-f Error Reporting Procedure

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
    api_instance = openapi_client.N32FErrorReportApi(api_client)
    n32f_error_info = openapi_client.N32fErrorInfo() # N32fErrorInfo | Custom operation for n32-f error reporting procedure

    try:
        # N32-f Error Reporting Procedure
        api_instance.post_n32f_error(n32f_error_info)
    except ApiException as e:
        print("Exception when calling N32FErrorReportApi->post_n32f_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n32f_error_info** | [**N32fErrorInfo**](N32fErrorInfo.md)| Custom operation for n32-f error reporting procedure | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful error reporting |  -  |
**400** | Bad request |  -  |
**411** | Length Required |  -  |
**413** | Payload Too Large |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

