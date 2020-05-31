from __future__ import print_function

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './openapi_client/')

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://example.com/n32c-handshake/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080/n32c-handshake/v1"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecurityCapabilityNegotiationApi(api_client)
    sec_negotiate_req_data = openapi_client.SecNegotiateReqData(sender="127.0.0.1", supported_sec_capability_list=["TLS", "string"])
    pprint(sec_negotiate_req_data)

    try:
        # N32-f Context Terminate
        api_response = api_instance.post_exchange_capability(sec_negotiate_req_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityCapabilityNegotiationApi->post_exchange_capability: %s\n" % e)

    
