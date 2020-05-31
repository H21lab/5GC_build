# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_negotiate_req_data import SecNegotiateReqData  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_negotiate_rsp_data import SecNegotiateRspData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSecurityCapabilityNegotiationController(BaseTestCase):
    """SecurityCapabilityNegotiationController integration test stubs"""

    def test_post_exchange_capability(self):
        """Test case for post_exchange_capability

        Security Capability Negotiation
        """
        sec_negotiate_req_data = {
  "sender" : "sender",
  "supportedSecCapabilityList" : [ null, null ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/n32c-handshake/v1/exchange-capability',
            method='POST',
            headers=headers,
            data=json.dumps(sec_negotiate_req_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
