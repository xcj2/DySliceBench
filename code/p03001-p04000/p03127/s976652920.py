#!/usr/bin/env python3

#
# Tips:
# - Use pbcopy command to copy this file to clipboard.
#

################################################################################

import math
from math import *
from math import factorial as fact
import itertools
from functools import reduce
#import numpy
#import scipy, scipy.special

def perm(a, b):
    import scipy.special
    return scipy.special.perm(a, b, exact = True)

def comb(a, b):
    import scipy.special
    return scipy.special.comb(a, b, exact = True)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_multi(l):
    return reduce(lambda x, y: gcd(x, y), l)

def input_ints(inp = input, sep = ' ', conv = lambda x: int(x)):
    return [conv(x) for x in inp().split(sep = sep)]

################################################################################

N = input_ints()
A = input_ints()

print(gcd_multi(A))
