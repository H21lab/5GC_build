# openapi_client.ParameterExchangeApi

All URIs are relative to *https://example.com/n32c-handshake/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_exchange_params**](ParameterExchangeApi.md#post_exchange_params) | **POST** /exchange-params | Parameter Exchange


# **post_exchange_params**
> SecParamExchRspData post_exchange_params(sec_param_exch_req_data)

Parameter Exchange

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
    api_instance = openapi_client.ParameterExchangeApi(api_client)
    sec_param_exch_req_data = openapi_client.SecParamExchReqData() # SecParamExchReqData | Custom operation for parameter exchange

    try:
        # Parameter Exchange
        api_response = api_instance.post_exchange_params(sec_param_exch_req_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParameterExchangeApi->post_exchange_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_param_exch_req_data** | [**SecParamExchReqData**](SecParamExchReqData.md)| Custom operation for parameter exchange | 

### Return type

[**SecParamExchRspData**](SecParamExchRspData.md)

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

