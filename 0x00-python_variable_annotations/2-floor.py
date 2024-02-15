#!/usr/bin/python3
"""florr function"""


def floor(n: float) -> float:
    """takes a float arguement and returns float"""

    if n >= 0:
        return int (n)
    else:
        return int(n - 1)
