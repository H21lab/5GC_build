# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class Snssai(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sst=None, sd=None):  # noqa: E501
        """Snssai - a model defined in OpenAPI

        :param sst: The sst of this Snssai.  # noqa: E501
        :type sst: int
        :param sd: The sd of this Snssai.  # noqa: E501
        :type sd: str
        """
        self.openapi_types = {
            'sst': int,
            'sd': str
        }

        self.attribute_map = {
            'sst': 'sst',
            'sd': 'sd'
        }

        self._sst = sst
        self._sd = sd

    @classmethod
    def from_dict(cls, dikt) -> 'Snssai':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Snssai of this Snssai.  # noqa: E501
        :rtype: Snssai
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sst(self):
        """Gets the sst of this Snssai.


        :return: The sst of this Snssai.
        :rtype: int
        """
        return self._sst

    @sst.setter
    def sst(self, sst):
        """Sets the sst of this Snssai.


        :param sst: The sst of this Snssai.
        :type sst: int
        """
        if sst is None:
            raise ValueError("Invalid value for `sst`, must not be `None`")  # noqa: E501
        if sst is not None and sst > 255:  # noqa: E501
            raise ValueError("Invalid value for `sst`, must be a value less than or equal to `255`")  # noqa: E501
        if sst is not None and sst < 0:  # noqa: E501
            raise ValueError("Invalid value for `sst`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sst = sst

    @property
    def sd(self):
        """Gets the sd of this Snssai.


        :return: The sd of this Snssai.
        :rtype: str
        """
        return self._sd

    @sd.setter
    def sd(self, sd):
        """Sets the sd of this Snssai.


        :param sd: The sd of this Snssai.
        :type sd: str
        """
        if sd is not None and not re.search(r'^[A-Fa-f0-9]{6}$', sd):  # noqa: E501
            raise ValueError("Invalid value for `sd`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{6}$/`")  # noqa: E501

        self._sd = sd
