#!/usr/bin/python3
""" Module of load from json """

import json


def load_from_json_file(filename):
    """ load a json from a file """
    with open(filename, encoding='utf-8') as f:
        return (json.loads(f.read()))
