# coding: utf-8

"""
    NRF NFDiscovery Service

    NRF NFDiscovery Service. © 2020, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.   # noqa: E501

    The version of the OpenAPI document: 1.1.0.alpha-4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from com.h21lab.TS29510_Nnrf_NFDiscovery.model.stored_search__document_api import StoredSearchDocumentApi  # noqa: E501
from openapi_client.rest import ApiException


class TestStoredSearchDocumentApi(unittest.TestCase):
    """StoredSearchDocumentApi unit test stubs"""

    def setUp(self):
        self.api = com.h21lab.TS29510_Nnrf_NFDiscovery.model.stored_search__document_api.StoredSearchDocumentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_stored_search(self):
        """Test case for retrieve_stored_search

        """
        pass


if __name__ == '__main__':
    unittest.main()
