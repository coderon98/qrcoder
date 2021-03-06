# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class VcardSchema(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, firstname=None, lastname=None, numero=None, fixe=None, fax=None, email=None, society=None, job=None, address=None, city=None, zipcode=None, state=None, country=None, website=None, frame=None, shape=None, logo=None):  # noqa: E501
        """VcardSchema - a model defined in OpenAPI

        :param firstname: The firstname of this VcardSchema.  # noqa: E501
        :type firstname: str
        :param lastname: The lastname of this VcardSchema.  # noqa: E501
        :type lastname: str
        :param numero: The numero of this VcardSchema.  # noqa: E501
        :type numero: str
        :param fixe: The fixe of this VcardSchema.  # noqa: E501
        :type fixe: str
        :param fax: The fax of this VcardSchema.  # noqa: E501
        :type fax: str
        :param email: The email of this VcardSchema.  # noqa: E501
        :type email: str
        :param society: The society of this VcardSchema.  # noqa: E501
        :type society: str
        :param job: The job of this VcardSchema.  # noqa: E501
        :type job: str
        :param address: The address of this VcardSchema.  # noqa: E501
        :type address: str
        :param city: The city of this VcardSchema.  # noqa: E501
        :type city: str
        :param zipcode: The zipcode of this VcardSchema.  # noqa: E501
        :type zipcode: str
        :param state: The state of this VcardSchema.  # noqa: E501
        :type state: str
        :param country: The country of this VcardSchema.  # noqa: E501
        :type country: str
        :param website: The website of this VcardSchema.  # noqa: E501
        :type website: str
        :param frame: The frame of this VcardSchema.  # noqa: E501
        :type frame: str
        :param shape: The shape of this VcardSchema.  # noqa: E501
        :type shape: str
        :param logo: The logo of this VcardSchema.  # noqa: E501
        :type logo: str
        """
        self.openapi_types = {
            'firstname': str,
            'lastname': str,
            'numero': str,
            'fixe': str,
            'fax': str,
            'email': str,
            'society': str,
            'job': str,
            'address': str,
            'city': str,
            'zipcode': str,
            'state': str,
            'country': str,
            'website': str,
            'frame': str,
            'shape': str,
            'logo': str
        }

        self.attribute_map = {
            'firstname': 'firstname',
            'lastname': 'lastname',
            'numero': 'numero',
            'fixe': 'fixe',
            'fax': 'fax',
            'email': 'email',
            'society': 'society',
            'job': 'job',
            'address': 'address',
            'city': 'city',
            'zipcode': 'zipcode',
            'state': 'state',
            'country': 'country',
            'website': 'website',
            'frame': 'frame',
            'shape': 'shape',
            'logo': 'logo'
        }

        self._firstname = firstname
        self._lastname = lastname
        self._numero = numero
        self._fixe = fixe
        self._fax = fax
        self._email = email
        self._society = society
        self._job = job
        self._address = address
        self._city = city
        self._zipcode = zipcode
        self._state = state
        self._country = country
        self._website = website
        self._frame = frame
        self._shape = shape
        self._logo = logo

    @classmethod
    def from_dict(cls, dikt) -> 'VcardSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vcardSchema of this VcardSchema.  # noqa: E501
        :rtype: VcardSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def firstname(self):
        """Gets the firstname of this VcardSchema.


        :return: The firstname of this VcardSchema.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this VcardSchema.


        :param firstname: The firstname of this VcardSchema.
        :type firstname: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this VcardSchema.


        :return: The lastname of this VcardSchema.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this VcardSchema.


        :param lastname: The lastname of this VcardSchema.
        :type lastname: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501

        self._lastname = lastname

    @property
    def numero(self):
        """Gets the numero of this VcardSchema.


        :return: The numero of this VcardSchema.
        :rtype: str
        """
        return self._numero

    @numero.setter
    def numero(self, numero):
        """Sets the numero of this VcardSchema.


        :param numero: The numero of this VcardSchema.
        :type numero: str
        """
        if numero is None:
            raise ValueError("Invalid value for `numero`, must not be `None`")  # noqa: E501

        self._numero = numero

    @property
    def fixe(self):
        """Gets the fixe of this VcardSchema.


        :return: The fixe of this VcardSchema.
        :rtype: str
        """
        return self._fixe

    @fixe.setter
    def fixe(self, fixe):
        """Sets the fixe of this VcardSchema.


        :param fixe: The fixe of this VcardSchema.
        :type fixe: str
        """

        self._fixe = fixe

    @property
    def fax(self):
        """Gets the fax of this VcardSchema.


        :return: The fax of this VcardSchema.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this VcardSchema.


        :param fax: The fax of this VcardSchema.
        :type fax: str
        """

        self._fax = fax

    @property
    def email(self):
        """Gets the email of this VcardSchema.


        :return: The email of this VcardSchema.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this VcardSchema.


        :param email: The email of this VcardSchema.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def society(self):
        """Gets the society of this VcardSchema.


        :return: The society of this VcardSchema.
        :rtype: str
        """
        return self._society

    @society.setter
    def society(self, society):
        """Sets the society of this VcardSchema.


        :param society: The society of this VcardSchema.
        :type society: str
        """

        self._society = society

    @property
    def job(self):
        """Gets the job of this VcardSchema.


        :return: The job of this VcardSchema.
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this VcardSchema.


        :param job: The job of this VcardSchema.
        :type job: str
        """

        self._job = job

    @property
    def address(self):
        """Gets the address of this VcardSchema.


        :return: The address of this VcardSchema.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this VcardSchema.


        :param address: The address of this VcardSchema.
        :type address: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this VcardSchema.


        :return: The city of this VcardSchema.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this VcardSchema.


        :param city: The city of this VcardSchema.
        :type city: str
        """

        self._city = city

    @property
    def zipcode(self):
        """Gets the zipcode of this VcardSchema.


        :return: The zipcode of this VcardSchema.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this VcardSchema.


        :param zipcode: The zipcode of this VcardSchema.
        :type zipcode: str
        """

        self._zipcode = zipcode

    @property
    def state(self):
        """Gets the state of this VcardSchema.


        :return: The state of this VcardSchema.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VcardSchema.


        :param state: The state of this VcardSchema.
        :type state: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this VcardSchema.


        :return: The country of this VcardSchema.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this VcardSchema.


        :param country: The country of this VcardSchema.
        :type country: str
        """

        self._country = country

    @property
    def website(self):
        """Gets the website of this VcardSchema.


        :return: The website of this VcardSchema.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this VcardSchema.


        :param website: The website of this VcardSchema.
        :type website: str
        """

        self._website = website

    @property
    def frame(self):
        """Gets the frame of this VcardSchema.


        :return: The frame of this VcardSchema.
        :rtype: str
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this VcardSchema.


        :param frame: The frame of this VcardSchema.
        :type frame: str
        """

        self._frame = frame

    @property
    def shape(self):
        """Gets the shape of this VcardSchema.


        :return: The shape of this VcardSchema.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this VcardSchema.


        :param shape: The shape of this VcardSchema.
        :type shape: str
        """

        self._shape = shape

    @property
    def logo(self):
        """Gets the logo of this VcardSchema.


        :return: The logo of this VcardSchema.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this VcardSchema.


        :param logo: The logo of this VcardSchema.
        :type logo: str
        """

        self._logo = logo
