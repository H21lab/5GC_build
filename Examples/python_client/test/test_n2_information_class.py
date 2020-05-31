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
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.n2_information_class import N2InformationClass  # noqa: E501
from openapi_client.rest import ApiException

class TestN2InformationClass(unittest.TestCase):
    """N2InformationClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test N2InformationClass
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.n2_information_class.N2InformationClass()  # noqa: E501
        if include_optional :
            return N2InformationClass(
            )
        else :
            return N2InformationClass(
        )

    def testN2InformationClass(self):
        """Test N2InformationClass"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
