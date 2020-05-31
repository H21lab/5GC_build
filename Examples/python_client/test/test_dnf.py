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
from openapi_client.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf import Dnf  # noqa: E501
from openapi_client.rest import ApiException

class TestDnf(unittest.TestCase):
    """Dnf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Dnf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.dnf.Dnf()  # noqa: E501
        if include_optional :
            return Dnf(
                dnf_units = [
                    openapi_client.models.dnf_unit.DnfUnit(
                        dnf_unit = [
                            openapi_client.models.atom.Atom(
                                attr = '0', 
                                value = null, 
                                negative = True, )
                            ], )
                    ]
            )
        else :
            return Dnf(
                dnf_units = [
                    openapi_client.models.dnf_unit.DnfUnit(
                        dnf_unit = [
                            openapi_client.models.atom.Atom(
                                attr = '0', 
                                value = null, 
                                negative = True, )
                            ], )
                    ],
        )

    def testDnf(self):
        """Test Dnf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
