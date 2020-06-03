#!/usr/bin/python3
""" module for json to string """

import json


def from_json_string(my_str):
    """ Loads json to str """
    return json.loads(my_str)
