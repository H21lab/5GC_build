# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.access_type import AccessType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.af_event_exposure_data import AfEventExposureData  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.an_node_type import AnNodeType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atsss_capability import AtsssCapability  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.complex_query import ComplexQuery  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.data_set_id import DataSetId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.event_id import EventId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.external_client_type import ExternalClientType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.guami import Guami  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_prefix import Ipv6Prefix  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nf_type import NFType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.notification_type import NotificationType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.nwdaf_event import NwdafEvent  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pdu_session_type import PduSessionType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.pfd_data import PfdData  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id import PlmnId  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_id_nid import PlmnIdNid  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.plmn_snssai import PlmnSnssai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.rat_type import RatType  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.search_result import SearchResult  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.service_name import ServiceName  # noqa: E501
java.util.*  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.snssai import Snssai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tai import Tai  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.tngf_info import TngfInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.twif_info import TwifInfo  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.w_agf_info import WAgfInfo  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNFInstancesStoreController(BaseTestCase):
    """NFInstancesStoreController integration test stubs"""

    def test_search_nf_instances(self):
        """Test case for search_nf_instances

        Search a collection of NF Instances
        """
        query_string = [('target-nf-type', {}),
                        ('requester-nf-type', {}),
                        ('requester-nf-instance-id', 'requester_nf_instance_id_example'),
                        ('service-names', {}),
                        ('requester-nf-instance-fqdn', 'requester_nf_instance_fqdn_example'),
                        ('target-plmn-list', {}),
                        ('requester-plmn-list', {}),
                        ('target-nf-instance-id', 'target_nf_instance_id_example'),
                        ('target-nf-fqdn', 'target_nf_fqdn_example'),
                        ('hnrf-uri', 'hnrf_uri_example'),
                        ('snssais', {}),
                        ('requester-snssais', {}),
                        ('plmn-specific-snssai-list', {}),
                        ('dnn', 'dnn_example'),
                        ('nsi-list', 'nsi_list_example'),
                        ('smf-serving-area', 'smf_serving_area_example'),
                        ('tai', {}),
                        ('amf-region-id', 'amf_region_id_example'),
                        ('amf-set-id', 'amf_set_id_example'),
                        ('guami', {}),
                        ('supi', 'supi_example'),
                        ('ue-ipv4-address', 'ue_ipv4_address_example'),
                        ('ip-domain', 'ip_domain_example'),
                        ('ue-ipv6-prefix', {}),
                        ('pgw-ind', True),
                        ('pgw', 'pgw_example'),
                        ('gpsi', 'gpsi_example'),
                        ('external-group-identity', 'external_group_identity_example'),
                        ('internal-group-identity', 'internal_group_identity_example'),
                        ('pfd-data', {}),
                        ('data-set', {}),
                        ('routing-indicator', 'routing_indicator_example'),
                        ('group-id-list', 'group_id_list_example'),
                        ('dnai-list', 'dnai_list_example'),
                        ('pdu-session-types', {}),
                        ('event-id-list', {}),
                        ('nwdaf-event-list', {}),
                        ('supported-features', 'supported_features_example'),
                        ('upf-iwk-eps-ind', True),
                        ('chf-supported-plmn', {}),
                        ('preferred-locality', 'preferred_locality_example'),
                        ('access-type', {}),
                        ('limit', 2),
                        ('required-features', 'required_features_example'),
                        ('complex-query', {}),
                        ('max-payload-size', 124),
                        ('atsss-capability', {}),
                        ('upf-ue-ip-addr-ind', True),
                        ('client-type', {}),
                        ('lmf-id', 'lmf_id_example'),
                        ('an-node-type', {}),
                        ('rat-type', {}),
                        ('preferred-tai', {}),
                        ('preferred-nf-instances', 'preferred_nf_instances_example'),
                        ('target-snpn', {}),
                        ('af-ee-data', {}),
                        ('w-agf-info', {}),
                        ('tngf-info', {}),
                        ('twif-info', {}),
                        ('target-nf-set-id', 'target_nf_set_id_example'),
                        ('target-nf-service-set-id', 'target_nf_service_set_id_example'),
                        ('nef-id', 'nef_id_example'),
                        ('notification-type', {}),
                        ('serving-scope', 'serving_scope_example'),
                        ('imsi', 'imsi_example'),
                        ('preferred-api-versions', {'key': 'preferred_api_versions_example'}),
                        ('v2x-support-ind', True),
                        ('redundant-gtpu', True),
                        ('redundant-transport', True)]
        headers = { 
            'Accept': 'application/json',
            'accept_encoding': 'accept_encoding_example',
            'if_none_match': 'if_none_match_example',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/nnrf-disc/v1/nf-instances',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
