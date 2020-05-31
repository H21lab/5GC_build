# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_param_exch_req_data import SecParamExchReqData  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_param_exch_rsp_data import SecParamExchRspData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestParameterExchangeController(BaseTestCase):
    """ParameterExchangeController integration test stubs"""

    def test_post_exchange_params(self):
        """Test case for post_exchange_params

        Parameter Exchange
        """
        sec_param_exch_req_data = {
  "n32fContextId" : "n32fContextId",
  "sender" : "sender",
  "jwsCipherSuiteList" : [ "jwsCipherSuiteList", "jwsCipherSuiteList" ],
  "protectionPolicyInfo" : {
    "apiIeMappingList" : [ {
      "IeList" : [ {
        "rspIe" : "rspIe",
        "reqIe" : "reqIe",
        "isModifiable" : true
      }, {
        "rspIe" : "rspIe",
        "reqIe" : "reqIe",
        "isModifiable" : true
      } ]
    }, {
      "IeList" : [ {
        "rspIe" : "rspIe",
        "reqIe" : "reqIe",
        "isModifiable" : true
      }, {
        "rspIe" : "rspIe",
        "reqIe" : "reqIe",
        "isModifiable" : true
      } ]
    } ],
    "dataTypeEncPolicy" : [ null, null ]
  },
  "jweCipherSuiteList" : [ "jweCipherSuiteList", "jweCipherSuiteList" ],
  "ipxProviderSecInfoList" : [ {
    "rawPublicKeyList" : [ "rawPublicKeyList", "rawPublicKeyList" ],
    "ipxProviderId" : "ipxProviderId",
    "certificateList" : [ "certificateList", "certificateList" ]
  }, {
    "rawPublicKeyList" : [ "rawPublicKeyList", "rawPublicKeyList" ],
    "ipxProviderId" : "ipxProviderId",
    "certificateList" : [ "certificateList", "certificateList" ]
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/n32c-handshake/v1/exchange-params',
            method='POST',
            headers=headers,
            data=json.dumps(sec_param_exch_req_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
