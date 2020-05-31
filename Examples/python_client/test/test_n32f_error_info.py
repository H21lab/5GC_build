# coding: utf-8

"""
    N32 Handshake API

    N32-c Handshake Service.  © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).  All rights reserved.   # noqa: E501

    The version of the OpenAPI document: 1.1.0.alpha-3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.com.h21lab.TS29573_N32_Handshake.handler.n32f_error_info import N32fErrorInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestN32fErrorInfo(unittest.TestCase):
    """N32fErrorInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test N32fErrorInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.n32f_error_info.N32fErrorInfo()  # noqa: E501
        if include_optional :
            return N32fErrorInfo(
                n32f_message_id = '0', 
                n32f_error_type = null, 
                failed_modification_list = [
                    openapi_client.models.failed_modification_info.FailedModificationInfo(
                        ipx_id = '0', 
                        n32f_error_type = null, )
                    ], 
                error_details_list = [
                    openapi_client.models.n32f_error_detail.N32fErrorDetail(
                        attribute = '0', 
                        msg_reconstruct_fail_reason = null, )
                    ]
            )
        else :
            return N32fErrorInfo(
                n32f_message_id = '0',
                n32f_error_type = null,
        )

    def testN32fErrorInfo(self):
        """Test N32fErrorInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
