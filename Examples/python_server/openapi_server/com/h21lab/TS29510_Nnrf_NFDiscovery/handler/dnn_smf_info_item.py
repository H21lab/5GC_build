# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server import util


class DnnSmfInfoItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dnn=None):  # noqa: E501
        """DnnSmfInfoItem - a model defined in OpenAPI

        :param dnn: The dnn of this DnnSmfInfoItem.  # noqa: E501
        :type dnn: str
        """
        self.openapi_types = {
            'dnn': str
        }

        self.attribute_map = {
            'dnn': 'dnn'
        }

        self._dnn = dnn

    @classmethod
    def from_dict(cls, dikt) -> 'DnnSmfInfoItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DnnSmfInfoItem of this DnnSmfInfoItem.  # noqa: E501
        :rtype: DnnSmfInfoItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dnn(self):
        """Gets the dnn of this DnnSmfInfoItem.


        :return: The dnn of this DnnSmfInfoItem.
        :rtype: str
        """
        return self._dnn

    @dnn.setter
    def dnn(self, dnn):
        """Sets the dnn of this DnnSmfInfoItem.


        :param dnn: The dnn of this DnnSmfInfoItem.
        :type dnn: str
        """
        if dnn is None:
            raise ValueError("Invalid value for `dnn`, must not be `None`")  # noqa: E501

        self._dnn = dnn
