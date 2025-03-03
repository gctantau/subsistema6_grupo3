# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.recambios_links import RecambiosLinks  # noqa: F401,E501
from swagger_server import util


class Recambios(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, taller_id: int=None, ref: int=None, unidades: int=None, links: RecambiosLinks=None):  # noqa: E501
        """Recambios - a model defined in Swagger

        :param id: The id of this Recambios.  # noqa: E501
        :type id: int
        :param taller_id: The taller_id of this Recambios.  # noqa: E501
        :type taller_id: int
        :param ref: The ref of this Recambios.  # noqa: E501
        :type ref: int
        :param unidades: The unidades of this Recambios.  # noqa: E501
        :type unidades: int
        :param links: The links of this Recambios.  # noqa: E501
        :type links: RecambiosLinks
        """
        self.swagger_types = {
            'id': int,
            'taller_id': int,
            'ref': int,
            'unidades': int,
            'links': RecambiosLinks
        }

        self.attribute_map = {
            'id': 'id',
            'taller_id': 'tallerId',
            'ref': 'ref',
            'unidades': 'unidades',
            'links': 'links'
        }
        self._id = id
        self._taller_id = taller_id
        self._ref = ref
        self._unidades = unidades
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'Recambios':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Recambios of this Recambios.  # noqa: E501
        :rtype: Recambios
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Recambios.

        Id pieza de recambio  # noqa: E501

        :return: The id of this Recambios.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Recambios.

        Id pieza de recambio  # noqa: E501

        :param id: The id of this Recambios.
        :type id: int
        """

        self._id = id

    @property
    def taller_id(self) -> int:
        """Gets the taller_id of this Recambios.

        taller Id  # noqa: E501

        :return: The taller_id of this Recambios.
        :rtype: int
        """
        return self._taller_id

    @taller_id.setter
    def taller_id(self, taller_id: int):
        """Sets the taller_id of this Recambios.

        taller Id  # noqa: E501

        :param taller_id: The taller_id of this Recambios.
        :type taller_id: int
        """

        self._taller_id = taller_id

    @property
    def ref(self) -> int:
        """Gets the ref of this Recambios.

        Ref. del artículo solicitado  # noqa: E501

        :return: The ref of this Recambios.
        :rtype: int
        """
        return self._ref

    @ref.setter
    def ref(self, ref: int):
        """Sets the ref of this Recambios.

        Ref. del artículo solicitado  # noqa: E501

        :param ref: The ref of this Recambios.
        :type ref: int
        """

        self._ref = ref

    @property
    def unidades(self) -> int:
        """Gets the unidades of this Recambios.

        Número de unidades de la referencia  # noqa: E501

        :return: The unidades of this Recambios.
        :rtype: int
        """
        return self._unidades

    @unidades.setter
    def unidades(self, unidades: int):
        """Sets the unidades of this Recambios.

        Número de unidades de la referencia  # noqa: E501

        :param unidades: The unidades of this Recambios.
        :type unidades: int
        """

        self._unidades = unidades

    @property
    def links(self) -> RecambiosLinks:
        """Gets the links of this Recambios.


        :return: The links of this Recambios.
        :rtype: RecambiosLinks
        """
        return self._links

    @links.setter
    def links(self, links: RecambiosLinks):
        """Sets the links of this Recambios.


        :param links: The links of this Recambios.
        :type links: RecambiosLinks
        """

        self._links = links
