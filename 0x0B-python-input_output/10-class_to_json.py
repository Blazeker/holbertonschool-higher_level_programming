#!/usr/bin/python3
""" Module for class to json """

import json


def class_to_json(obj):
    """ return obj dictionary """
    return obj.__dict__
