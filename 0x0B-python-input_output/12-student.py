#!/usr/bin/python3
""" Module for student class """


class Student():
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) != list:
            return self.__dict__
        else:
            dictatr = {}
            for i in attrs:
                if type(i) == str:
                    if i in self.__dict__.keys():
                        dictatr[i] = self.__dict__.get(i)
            return dictatr
