# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.base_model_ import Model
from openapi_server import util


class IeType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """IeType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'IeType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IeType of this IeType.  # noqa: E501
        :rtype: IeType
        """
        return util.deserialize_model(dikt, cls)
