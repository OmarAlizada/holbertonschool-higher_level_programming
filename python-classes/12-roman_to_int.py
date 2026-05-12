#!/usr/bin/python3
"""Roma rəqəmləri modulu"""


def roman_to_int(roman_string):
    """Roma rəqəmlərini tam ədədə çevirən funksiya"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res, prev = 0, 0
    for c in reversed(roman_string):
        val = d.get(c, 0)
        res += val if val >= prev else -val
        prev = val
    return res
