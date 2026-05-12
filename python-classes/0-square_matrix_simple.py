#!/usr/bin/python3
"""Kvadrat matris modulu"""


def square_matrix_simple(matrix=[]):
    """Bütün tam ədədlərin kvadratını hesablayan funksiya"""
    return [[element ** 2 for element in row] for row in matrix]
