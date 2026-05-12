#!/usr/bin/python3
"""Ən yaxşı nəticə modulu"""


def best_score(a_dictionary):
    """Ən böyük dəyərə sahib açarı tapan funksiya"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
