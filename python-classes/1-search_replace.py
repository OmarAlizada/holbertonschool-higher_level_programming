#!/usr/bin/python3
"""Axtar və əvəzlə modulu"""


def search_replace(my_list, search, replace):
    """Elementi yenisi ilə əvəz edən funksiya"""
    return [replace if element == search else element for element in my_list]
