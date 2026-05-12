#!/usr/bin/python3
"""Element silmə modulu"""


def simple_delete(a_dictionary, key=""):
    """Müəyyən açarı silən funksiya"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
