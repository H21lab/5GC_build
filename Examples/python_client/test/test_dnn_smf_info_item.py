# coding: utf-8

"""
    NRF NFDiscovery Service

    NRF NFDiscovery Service. © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.   # noqa: E501

    The version of the OpenAPI document: 1.1.0.alpha-4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnn_smf_info_item import DnnSmfInfoItem  # noqa: E501
from openapi_client.rest import ApiException

class TestDnnSmfInfoItem(unittest.TestCase):
    """DnnSmfInfoItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DnnSmfInfoItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.dnn_smf_info_item.DnnSmfInfoItem()  # noqa: E501
        if include_optional :
            return DnnSmfInfoItem(
                dnn = '0'
            )
        else :
            return DnnSmfInfoItem(
                dnn = '0',
        )

    def testDnnSmfInfoItem(self):
        """Test DnnSmfInfoItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
