# openapi_client.StoredSearchDocumentApi

All URIs are relative to *https://example.com/nnrf-disc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_stored_search**](StoredSearchDocumentApi.md#retrieve_stored_search) | **GET** /searches/{searchId} | 


# **retrieve_stored_search**
> StoredSearchResult retrieve_stored_search(search_id, accept_encoding=accept_encoding)



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
    api_instance = openapi_client.StoredSearchDocumentApi(api_client)
    search_id = 'search_id_example' # str | Id of a stored search
accept_encoding = 'accept_encoding_example' # str | Accept-Encoding, described in IETF RFC 7231 (optional)

    try:
        api_response = api_instance.retrieve_stored_search(search_id, accept_encoding=accept_encoding)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoredSearchDocumentApi->retrieve_stored_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Id of a stored search | 
 **accept_encoding** | **str**| Accept-Encoding, described in IETF RFC 7231 | [optional] 

### Return type

[**StoredSearchResult**](StoredSearchResult.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  * Cache-Control - Cache-Control containing max-age, described in IETF RFC 7234, 5.2 <br>  * ETag - Entity Tag containing a strong validator, described in IETF RFC 7232, 2.3 <br>  * Content-Encoding - Content-Encoding, described in IETF RFC 7231 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

