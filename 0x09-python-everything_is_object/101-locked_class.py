#!/usr/bin/python3
""" Locked Class Module """


class LockedClass:
  """ Reduces the consumption of ram using slot to define only first_name attribute """
  __slots__ = ["first_name"]
