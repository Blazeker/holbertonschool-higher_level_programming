#!/usr/bin/python3
""" Base Module """


import json
import csv


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSON strings """
        if type(json_string) != str or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ Method that return a list of instances """
        list_aux = []
        with open(cls.__name__ + ".json", r) as f:
            inst = f.read()
        inst = cls.from_json_string(inst)
        for i in inst:
            if type(i) == dict:
                list_aux.append(cls.create(**i))
            else:
                list_aux(i)
        return list_aux

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None or list_objs == []:
                csvfile.write("[]")
        with open(cls.__name__ + ".csv", "w",) as f:
            if cls.__name__ == "Rectangle":
                field_names = ["id", "width", "height", "x", "y"]
            else:
                field_names = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=field_names)
            for objs in list_objs:
                writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        res = []
        dic = {}
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                if cls.__name__ == "Rectangle":
                    field_names = ['id', 'width', 'height', 'x', 'y']
                else:
                    field_names = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=field_names)
                for rows in reader:
                    for key, v in dict(rows).items():
                        dic[key] = int(v)
                    res.append(cls.create(**dic))
        except:
            return "[]"
        return res