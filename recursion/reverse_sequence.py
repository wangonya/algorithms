#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverse(S):
    """reverse elements in implicit slice S[start:stop]"""
    start = S[0]
    stop = S[-1]
    if start < stop - 1:  # if at least 2 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]  # swap first and last
        reverse(S, start + 1, stop - 1)
