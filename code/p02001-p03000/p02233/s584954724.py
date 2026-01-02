#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import math
import itertools
import functools
import logging

logging.basicConfig(level=logging.DEBUG, format="DBG: %(message)s")

def dbg(msg, *args, **kwargs):
    logging.debug(msg, *args, **kwargs)

def fib(n):
    assert n >= 0

    f0 = 1
    f1 = 1

    if n == 0: return f0
    if n == 1: return f1

    for _ in range(n-1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2

    return f2

def main():
    n = int(input())

    print(fib(n))

if __name__ == "__main__": main()