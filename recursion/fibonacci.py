#!/usr/bin/env python
# -*- coding: utf-8 -*-


#O(n!)
def bad_fibonacci(n):
    """return the nth fib number"""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

#O(n)
def good_fibonacci(n):
    """return a pair of fib numbers, f(n) and f(n-1)"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)
