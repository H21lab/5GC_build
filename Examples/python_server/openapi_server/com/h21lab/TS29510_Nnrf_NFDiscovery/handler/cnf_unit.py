# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atom import Atom
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.atom import Atom  # noqa: E501

class CnfUnit(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cnf_unit=None):  # noqa: E501
        """CnfUnit - a model defined in OpenAPI

        :param cnf_unit: The cnf_unit of this CnfUnit.  # noqa: E501
        :type cnf_unit: List[Atom]
        """
        self.openapi_types = {
            'cnf_unit': List[Atom]
        }

        self.attribute_map = {
            'cnf_unit': 'cnfUnit'
        }

        self._cnf_unit = cnf_unit

    @classmethod
    def from_dict(cls, dikt) -> 'CnfUnit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CnfUnit of this CnfUnit.  # noqa: E501
        :rtype: CnfUnit
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cnf_unit(self):
        """Gets the cnf_unit of this CnfUnit.


        :return: The cnf_unit of this CnfUnit.
        :rtype: List[Atom]
        """
        return self._cnf_unit

    @cnf_unit.setter
    def cnf_unit(self, cnf_unit):
        """Sets the cnf_unit of this CnfUnit.


        :param cnf_unit: The cnf_unit of this CnfUnit.
        :type cnf_unit: List[Atom]
        """
        if cnf_unit is None:
            raise ValueError("Invalid value for `cnf_unit`, must not be `None`")  # noqa: E501

        self._cnf_unit = cnf_unit
