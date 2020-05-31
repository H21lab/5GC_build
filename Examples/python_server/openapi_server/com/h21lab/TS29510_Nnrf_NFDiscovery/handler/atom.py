# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.base_model_ import Model
from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.any_type import AnyType
from openapi_server import util

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.any_type import AnyType  # noqa: E501

class Atom(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attr=None, value=None, negative=None):  # noqa: E501
        """Atom - a model defined in OpenAPI

        :param attr: The attr of this Atom.  # noqa: E501
        :type attr: str
        :param value: The value of this Atom.  # noqa: E501
        :type value: AnyType
        :param negative: The negative of this Atom.  # noqa: E501
        :type negative: bool
        """
        self.openapi_types = {
            'attr': str,
            'value': AnyType,
            'negative': bool
        }

        self.attribute_map = {
            'attr': 'attr',
            'value': 'value',
            'negative': 'negative'
        }

        self._attr = attr
        self._value = value
        self._negative = negative

    @classmethod
    def from_dict(cls, dikt) -> 'Atom':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Atom of this Atom.  # noqa: E501
        :rtype: Atom
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attr(self):
        """Gets the attr of this Atom.


        :return: The attr of this Atom.
        :rtype: str
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        """Sets the attr of this Atom.


        :param attr: The attr of this Atom.
        :type attr: str
        """
        if attr is None:
            raise ValueError("Invalid value for `attr`, must not be `None`")  # noqa: E501

        self._attr = attr

    @property
    def value(self):
        """Gets the value of this Atom.


        :return: The value of this Atom.
        :rtype: AnyType
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Atom.


        :param value: The value of this Atom.
        :type value: AnyType
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def negative(self):
        """Gets the negative of this Atom.


        :return: The negative of this Atom.
        :rtype: bool
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """Sets the negative of this Atom.


        :param negative: The negative of this Atom.
        :type negative: bool
        """

        self._negative = negative