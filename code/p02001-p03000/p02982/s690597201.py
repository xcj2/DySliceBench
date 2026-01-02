#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  # {{{
import os
import time
import re
from pydoc import help
import string
import math
from operator import itemgetter
from collections import Counter
from collections import deque
from collections import defaultdict as dd
import fractions
from heapq import heappop, heappush, heapify
import array
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy as dcopy
import itertools
# }}}

# pre-defined{{{
sys.setrecursionlimit(10**7)
INF = 10**20
GOSA = 1.0 / 10**10
MOD = 10**9+7
ALPHABETS = [chr(i) for i in range(ord('a'), ord('z')+1)]  # can also use string module
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def DP(N, M, first): return [[first] * M for n in range(N)]
def DP3(N, M, L, first): return [[[first] * L for n in range(M)] for _ in range(N)]
from inspect import currentframe
# }}}

def local_input():# {{{
    from pcm.utils import set_stdin
    import sys
    from pathlib import Path
    parentdir = Path(os.path.dirname(__file__)).parent
    inputfile = parentdir.joinpath('test/sample-1.in')
    if len(sys.argv) == 1:
        set_stdin(inputfile)
# }}}

def solve():
    n,d = map(int,input().split())
    lst = [0]*n
    for i in range(n):
        lst[i] = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum = 0
            for k in range(d):
                sum += (lst[j][k]-lst[i][k])**2
            if round(math.sqrt(sum))**2 == sum:
                ans +=1
    print(ans) 
    return 0

if __name__ == "__main__":# {{{
    try:
        local_input()
        def dump(*args):
            names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
            print(', '.join(names.get(id(arg),'???')+' => '+repr(arg) for arg in args), file=sys.stderr)
    except:
        def dump(*args):
            pass

    solve()

# vim: set foldmethod=marker:}}}
