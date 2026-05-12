#!/usr/bin/python3
"""2-yə vurma modulu"""


def multiply_by_2(a_dictionary):
    """Bütün dəyərləri 2-yə vuran funksiya"""
    return {key: value * 2 for key, value in a_dictionary.items()}
