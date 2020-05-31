# openapi-client
N32-c Handshake Service.
 © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).
 All rights reserved.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0.alpha-3
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with openapi_client.ApiClient(configuration) as api_client:
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

## Documentation for API Endpoints

All URIs are relative to *https://example.com/n32c-handshake/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*N32FContextTerminateApi* | [**post_n32f_terminate**](docs/N32FContextTerminateApi.md#post_n32f_terminate) | **POST** /n32f-terminate | N32-f Context Terminate
*N32FErrorReportApi* | [**post_n32f_error**](docs/N32FErrorReportApi.md#post_n32f_error) | **POST** /n32f-error | N32-f Error Reporting Procedure
*ParameterExchangeApi* | [**post_exchange_params**](docs/ParameterExchangeApi.md#post_exchange_params) | **POST** /exchange-params | Parameter Exchange
*SecurityCapabilityNegotiationApi* | [**post_exchange_capability**](docs/SecurityCapabilityNegotiationApi.md#post_exchange_capability) | **POST** /exchange-capability | Security Capability Negotiation


## Documentation For Models

 - [ApiIeMapping](docs/ApiIeMapping.md)
 - [ApiSignature](docs/ApiSignature.md)
 - [CallbackName](docs/CallbackName.md)
 - [FailedModificationInfo](docs/FailedModificationInfo.md)
 - [FailureReason](docs/FailureReason.md)
 - [HttpMethod](docs/HttpMethod.md)
 - [IeInfo](docs/IeInfo.md)
 - [IeLocation](docs/IeLocation.md)
 - [IeType](docs/IeType.md)
 - [InvalidParam](docs/InvalidParam.md)
 - [IpxProviderSecInfo](docs/IpxProviderSecInfo.md)
 - [N32fContextInfo](docs/N32fContextInfo.md)
 - [N32fErrorDetail](docs/N32fErrorDetail.md)
 - [N32fErrorInfo](docs/N32fErrorInfo.md)
 - [N32fErrorType](docs/N32fErrorType.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [ProtectionPolicy](docs/ProtectionPolicy.md)
 - [SecNegotiateReqData](docs/SecNegotiateReqData.md)
 - [SecNegotiateRspData](docs/SecNegotiateRspData.md)
 - [SecParamExchReqData](docs/SecParamExchReqData.md)
 - [SecParamExchRspData](docs/SecParamExchRspData.md)
 - [SecurityCapability](docs/SecurityCapability.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author



