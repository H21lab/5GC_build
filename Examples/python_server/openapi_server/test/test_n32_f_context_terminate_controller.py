# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.n32f_context_info import N32fContextInfo  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.test import BaseTestCase


class TestN32FContextTerminateController(BaseTestCase):
    """N32FContextTerminateController integration test stubs"""

    def test_post_n32f_terminate(self):
        """Test case for post_n32f_terminate

        N32-f Context Terminate
        """
        n32f_context_info = {
  "n32fContextId" : "n32fContextId"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/n32c-handshake/v1/n32f-terminate',
            method='POST',
            headers=headers,
            data=json.dumps(n32f_context_info),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
