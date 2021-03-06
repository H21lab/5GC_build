# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf_unit import CnfUnit
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.cnf_unit import CnfUnit  # noqa: E501

class Cnf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cnf_units=None):  # noqa: E501
        """Cnf - a model defined in OpenAPI

        :param cnf_units: The cnf_units of this Cnf.  # noqa: E501
        :type cnf_units: List[CnfUnit]
        """
        self.openapi_types = {
            'cnf_units': List[CnfUnit]
        }

        self.attribute_map = {
            'cnf_units': 'cnfUnits'
        }

        self._cnf_units = cnf_units

    @classmethod
    def from_dict(cls, dikt) -> 'Cnf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cnf of this Cnf.  # noqa: E501
        :rtype: Cnf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cnf_units(self):
        """Gets the cnf_units of this Cnf.


        :return: The cnf_units of this Cnf.
        :rtype: List[CnfUnit]
        """
        return self._cnf_units

    @cnf_units.setter
    def cnf_units(self, cnf_units):
        """Sets the cnf_units of this Cnf.


        :param cnf_units: The cnf_units of this Cnf.
        :type cnf_units: List[CnfUnit]
        """
        if cnf_units is None:
            raise ValueError("Invalid value for `cnf_units`, must not be `None`")  # noqa: E501

        self._cnf_units = cnf_units
