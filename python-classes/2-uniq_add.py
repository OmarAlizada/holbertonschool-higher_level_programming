#!/usr/bin/python3
"""Unikal toplama modulu"""


def uniq_add(my_list=[]):
    """Təkrarlanmayan ədədləri toplayan funksiya"""
    return sum(set(my_list))
