# coding: utf-8

"""
    Clever API

    The Clever API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from clever.models.event import Event  # noqa: F401,E501

class DistrictsUpdated(Event):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'DistrictObject',
        'previous_attributes': 'object'
    }
    if hasattr(Event, "swagger_types"):
        swagger_types.update(Event.swagger_types)

    attribute_map = {
        'data': 'data',
        'previous_attributes': 'previous_attributes'
    }
    if hasattr(Event, "attribute_map"):
        attribute_map.update(Event.attribute_map)

    def __init__(self, data=None, previous_attributes=None, *args, **kwargs):  # noqa: E501
        """DistrictsUpdated - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._previous_attributes = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if previous_attributes is not None:
            self.previous_attributes = previous_attributes
        Event.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Gets the data of this DistrictsUpdated.  # noqa: E501


        :return: The data of this DistrictsUpdated.  # noqa: E501
        :rtype: DistrictObject
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DistrictsUpdated.


        :param data: The data of this DistrictsUpdated.  # noqa: E501
        :type: DistrictObject
        """

        self._data = data

    @property
    def previous_attributes(self):
        """Gets the previous_attributes of this DistrictsUpdated.  # noqa: E501


        :return: The previous_attributes of this DistrictsUpdated.  # noqa: E501
        :rtype: object
        """
        return self._previous_attributes

    @previous_attributes.setter
    def previous_attributes(self, previous_attributes):
        """Sets the previous_attributes of this DistrictsUpdated.


        :param previous_attributes: The previous_attributes of this DistrictsUpdated.  # noqa: E501
        :type: object
        """

        self._previous_attributes = previous_attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DistrictsUpdated, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DistrictsUpdated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
