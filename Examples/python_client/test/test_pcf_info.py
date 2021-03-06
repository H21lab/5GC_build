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
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pcf_info import PcfInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestPcfInfo(unittest.TestCase):
    """PcfInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PcfInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pcf_info.PcfInfo()  # noqa: E501
        if include_optional :
            return PcfInfo(
                group_id = '0', 
                dnn_list = [
                    '0'
                    ], 
                supi_ranges = [
                    openapi_client.models.supi_range.SupiRange(
                        start = 'a', 
                        end = 'a', 
                        pattern = '0', )
                    ], 
                gpsi_ranges = [
                    openapi_client.models.identity_range.IdentityRange(
                        start = 'a', 
                        end = 'a', 
                        pattern = '0', )
                    ], 
                rx_diam_host = 'a', 
                rx_diam_realm = 'a', 
                v2x_support_ind = True
            )
        else :
            return PcfInfo(
        )

    def testPcfInfo(self):
        """Test PcfInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
