#!/usr/bin/python3
def max_integer(my_list=[]):
    """Siyahidaki en boyuk tam ededi tapir."""
    if not my_list:
        return None
    max_val = my_list[0]
    for x in my_list:
        if x > max_val:
            max_val = x
    return max_val
