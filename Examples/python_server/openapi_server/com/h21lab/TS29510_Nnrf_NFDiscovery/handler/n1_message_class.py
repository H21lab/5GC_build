# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server import util


class N1MessageClass(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """N1MessageClass - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'N1MessageClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The N1MessageClass of this N1MessageClass.  # noqa: E501
        :rtype: N1MessageClass
        """
        return util.deserialize_model(dikt, cls)
