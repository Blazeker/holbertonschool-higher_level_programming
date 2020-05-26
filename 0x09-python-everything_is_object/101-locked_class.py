#!/usr/bin/python3
""" Locked Class Module """


class LockedClass:
    """
    Reduces the compsution of ram locking only
    for anything but attributes called 'first_name'.
    """
  __slots__ = ["first_name"]
