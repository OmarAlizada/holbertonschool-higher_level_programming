#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """İki tuple-ın ilk iki elementini toplayıb yeni tuple qaytarır."""
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    res_1 = a[0] + b[0]
    res_2 = a[1] + b[1]
    return (res_1, res_2)
