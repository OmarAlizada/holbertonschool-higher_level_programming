#!/usr/bin/python3
"""Sıralanmış çap modulu"""


def print_sorted_dictionary(a_dictionary):
    """Lüğəti əlifba sırası ilə çap edən funksiya"""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
