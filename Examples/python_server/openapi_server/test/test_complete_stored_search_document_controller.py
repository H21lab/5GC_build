# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.stored_search_result import StoredSearchResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCompleteStoredSearchDocumentController(BaseTestCase):
    """CompleteStoredSearchDocumentController integration test stubs"""

    def test_retrieve_complete_search(self):
        """Test case for retrieve_complete_search

        
        """
        headers = { 
            'Accept': 'application/json',
            'accept_encoding': 'accept_encoding_example',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/nnrf-disc/v1/searches/{search_id}/complete'.format(search_id='search_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
