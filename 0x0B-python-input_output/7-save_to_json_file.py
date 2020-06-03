#!/usr/bin/python3
""" Module for json to file """

import json


def save_to_json_file(my_obj, filename):
    """ Save json into a file """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
