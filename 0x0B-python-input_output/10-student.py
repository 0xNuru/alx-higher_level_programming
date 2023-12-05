#!/usr/bin/python3
"""This module contains a Student class"""


class Student:
    """This class defines a student object"""

    def __init__(self, first_name, last_name, age):
        """
        Desc:
            constructor

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's ag3
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Desc:
            JSONify object
        Args:
            attrs
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        jsonify = self.__dict__
        return jsonify
