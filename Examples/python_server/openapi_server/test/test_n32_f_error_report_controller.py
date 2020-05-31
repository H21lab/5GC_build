# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.n32f_error_info import N32fErrorInfo  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.test import BaseTestCase


class TestN32FErrorReportController(BaseTestCase):
    """N32FErrorReportController integration test stubs"""

    def test_post_n32f_error(self):
        """Test case for post_n32f_error

        N32-f Error Reporting Procedure
        """
        n32f_error_info = {
  "n32fMessageId" : "n32fMessageId",
  "errorDetailsList" : [ {
    "attribute" : "attribute"
  }, {
    "attribute" : "attribute"
  } ],
  "failedModificationList" : [ {
    "ipxId" : "ipxId"
  }, {
    "ipxId" : "ipxId"
  } ]
}
        headers = { 
            'Accept': 'application/problem+json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/n32c-handshake/v1/n32f-error',
            method='POST',
            headers=headers,
            data=json.dumps(n32f_error_info),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
