#!/usr/bin/python3
"""Map vurma modulu"""


def multiply_list_map(my_list=[], number=0):
    """Map istifadə edərək siyahını vuran funksiya"""
    return list(map(lambda x: x * number, my_list))
