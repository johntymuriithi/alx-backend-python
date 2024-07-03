#!/usr/bin/env python3

"""Module that annotates the below function's parameters
    and return values with the appropriate types

-   def element_length(lst):
        return [(i, len(i)) for i in lst]
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes a list of strings
        and returns a list of tuples with the string
        and its length.
    """
    return [(i, len(i)) for i in lst]
