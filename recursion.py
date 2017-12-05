#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Week14"""


def fibonnaci(n):
    """Returns the nth element in the Fibonnaci sequence.
    Args:
        n (int): integer parameter
    Returns:
        the nth element in the Fibonnaci sequence
    Examples:
        >>> fibonnaci(1)
        1
        >>> fibonnaci(15)
        610
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    """Takes parameters a and b and returns the greatest common divisor.
    Args:
        a (int)
        b (int)
    Returns:
        the greatest common divisor
    Examples:
        >>> gcd(250, 100)
        50
        >>> gcd(65, 125)
        5
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """Compare two strings
    """
    if s1 == '' and s2 == '':
        return 0
    elif ord(s1[0]) > ord(s2[0]):
        return 0 + ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return 0 - ord(s2[0])
    elif s1[1:2] == '' and not s2[1:2] == '':
        return 0 - ord(s2[0])
    elif s2[1:2] == '' and not s1[1:2] == '':
        return 0 + ord(s1[0])
    elif s1[1:2] == '' and s2[1:2] == '':
        return 0
    else:
        return compareTo(s1[1:], s2[1:]);
