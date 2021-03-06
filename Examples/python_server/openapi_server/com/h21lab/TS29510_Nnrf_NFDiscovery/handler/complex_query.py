# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf import Cnf
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf_unit import CnfUnit
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf import Dnf
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf_unit import DnfUnit
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf import Cnf  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf_unit import CnfUnit  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf import Dnf  # noqa: E501
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.dnf_unit import DnfUnit  # noqa: E501

class ComplexQuery(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cnf_units=None, dnf_units=None):  # noqa: E501
        """ComplexQuery - a model defined in OpenAPI

        :param cnf_units: The cnf_units of this ComplexQuery.  # noqa: E501
        :type cnf_units: List[CnfUnit]
        :param dnf_units: The dnf_units of this ComplexQuery.  # noqa: E501
        :type dnf_units: List[DnfUnit]
        """
        self.openapi_types = {
            'cnf_units': List[CnfUnit],
            'dnf_units': List[DnfUnit]
        }

        self.attribute_map = {
            'cnf_units': 'cnfUnits',
            'dnf_units': 'dnfUnits'
        }

        self._cnf_units = cnf_units
        self._dnf_units = dnf_units

    @classmethod
    def from_dict(cls, dikt) -> 'ComplexQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComplexQuery of this ComplexQuery.  # noqa: E501
        :rtype: ComplexQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cnf_units(self):
        """Gets the cnf_units of this ComplexQuery.


        :return: The cnf_units of this ComplexQuery.
        :rtype: List[CnfUnit]
        """
        return self._cnf_units

    @cnf_units.setter
    def cnf_units(self, cnf_units):
        """Sets the cnf_units of this ComplexQuery.


        :param cnf_units: The cnf_units of this ComplexQuery.
        :type cnf_units: List[CnfUnit]
        """
        if cnf_units is None:
            raise ValueError("Invalid value for `cnf_units`, must not be `None`")  # noqa: E501

        self._cnf_units = cnf_units

    @property
    def dnf_units(self):
        """Gets the dnf_units of this ComplexQuery.


        :return: The dnf_units of this ComplexQuery.
        :rtype: List[DnfUnit]
        """
        return self._dnf_units

    @dnf_units.setter
    def dnf_units(self, dnf_units):
        """Sets the dnf_units of this ComplexQuery.


        :param dnf_units: The dnf_units of this ComplexQuery.
        :type dnf_units: List[DnfUnit]
        """
        if dnf_units is None:
            raise ValueError("Invalid value for `dnf_units`, must not be `None`")  # noqa: E501

        self._dnf_units = dnf_units
