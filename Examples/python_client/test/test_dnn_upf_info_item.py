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
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnn_upf_info_item import DnnUpfInfoItem  # noqa: E501
from openapi_client.rest import ApiException

class TestDnnUpfInfoItem(unittest.TestCase):
    """DnnUpfInfoItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DnnUpfInfoItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.dnn_upf_info_item.DnnUpfInfoItem()  # noqa: E501
        if include_optional :
            return DnnUpfInfoItem(
                dnn = '0', 
                dnai_list = [
                    '0'
                    ], 
                pdu_session_types = [
                    null
                    ], 
                ipv4_address_ranges = [
                    openapi_client.models.ipv4_address_range.Ipv4AddressRange(
                        start = '198.51.100.1', 
                        end = '198.51.100.1', )
                    ], 
                ipv6_prefix_ranges = [
                    openapi_client.models.ipv6_prefix_range.Ipv6PrefixRange(
                        start = '2001:db8:abcd:12::0/64', 
                        end = '2001:db8:abcd:12::0/64', )
                    ]
            )
        else :
            return DnnUpfInfoItem(
                dnn = '0',
        )

    def testDnnUpfInfoItem(self):
        """Test DnnUpfInfoItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
