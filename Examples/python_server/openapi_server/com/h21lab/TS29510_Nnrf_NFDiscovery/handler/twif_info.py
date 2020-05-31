# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_addr import Ipv6Addr
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.ipv6_addr import Ipv6Addr  # noqa: E501

class TwifInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4_endpoint_addresses=None, ipv6_endpoint_addresses=None, endpoint_fqdn=None):  # noqa: E501
        """TwifInfo - a model defined in OpenAPI

        :param ipv4_endpoint_addresses: The ipv4_endpoint_addresses of this TwifInfo.  # noqa: E501
        :type ipv4_endpoint_addresses: List[str]
        :param ipv6_endpoint_addresses: The ipv6_endpoint_addresses of this TwifInfo.  # noqa: E501
        :type ipv6_endpoint_addresses: List[Ipv6Addr]
        :param endpoint_fqdn: The endpoint_fqdn of this TwifInfo.  # noqa: E501
        :type endpoint_fqdn: str
        """
        self.openapi_types = {
            'ipv4_endpoint_addresses': List[str],
            'ipv6_endpoint_addresses': List[Ipv6Addr],
            'endpoint_fqdn': str
        }

        self.attribute_map = {
            'ipv4_endpoint_addresses': 'ipv4EndpointAddresses',
            'ipv6_endpoint_addresses': 'ipv6EndpointAddresses',
            'endpoint_fqdn': 'endpointFqdn'
        }

        self._ipv4_endpoint_addresses = ipv4_endpoint_addresses
        self._ipv6_endpoint_addresses = ipv6_endpoint_addresses
        self._endpoint_fqdn = endpoint_fqdn

    @classmethod
    def from_dict(cls, dikt) -> 'TwifInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TwifInfo of this TwifInfo.  # noqa: E501
        :rtype: TwifInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_endpoint_addresses(self):
        """Gets the ipv4_endpoint_addresses of this TwifInfo.


        :return: The ipv4_endpoint_addresses of this TwifInfo.
        :rtype: List[str]
        """
        return self._ipv4_endpoint_addresses

    @ipv4_endpoint_addresses.setter
    def ipv4_endpoint_addresses(self, ipv4_endpoint_addresses):
        """Sets the ipv4_endpoint_addresses of this TwifInfo.


        :param ipv4_endpoint_addresses: The ipv4_endpoint_addresses of this TwifInfo.
        :type ipv4_endpoint_addresses: List[str]
        """

        self._ipv4_endpoint_addresses = ipv4_endpoint_addresses

    @property
    def ipv6_endpoint_addresses(self):
        """Gets the ipv6_endpoint_addresses of this TwifInfo.


        :return: The ipv6_endpoint_addresses of this TwifInfo.
        :rtype: List[Ipv6Addr]
        """
        return self._ipv6_endpoint_addresses

    @ipv6_endpoint_addresses.setter
    def ipv6_endpoint_addresses(self, ipv6_endpoint_addresses):
        """Sets the ipv6_endpoint_addresses of this TwifInfo.


        :param ipv6_endpoint_addresses: The ipv6_endpoint_addresses of this TwifInfo.
        :type ipv6_endpoint_addresses: List[Ipv6Addr]
        """

        self._ipv6_endpoint_addresses = ipv6_endpoint_addresses

    @property
    def endpoint_fqdn(self):
        """Gets the endpoint_fqdn of this TwifInfo.

        Fully Qualified Domain Name  # noqa: E501

        :return: The endpoint_fqdn of this TwifInfo.
        :rtype: str
        """
        return self._endpoint_fqdn

    @endpoint_fqdn.setter
    def endpoint_fqdn(self, endpoint_fqdn):
        """Sets the endpoint_fqdn of this TwifInfo.

        Fully Qualified Domain Name  # noqa: E501

        :param endpoint_fqdn: The endpoint_fqdn of this TwifInfo.
        :type endpoint_fqdn: str
        """

        self._endpoint_fqdn = endpoint_fqdn
