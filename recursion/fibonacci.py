#!/usr/bin/env python
# -*- coding: utf-8 -*-


# O(n!)
def bad_fibonacci(n):
    """return the nth fib number"""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)


# O(n)
def good_fibonacci(n):
    """return a pair of fib numbers, f(n) and f(n-1)"""
    if n <= 1:
        print(f'n ==> {n}')
        return (n, 0)
    else:
        print(f'n ==> {n}')
        (a, b) = good_fibonacci(n - 1)
        print(f'a,b ==> {(a,b)}')
        return (a + b, a)
