#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n=int(input())
    A=list(map(int,input().split()))

    from functools import reduce
    from math import gcd
    
    def lcm(A, B):
        return A * B // gcd(A, B)
    
    
    # リストを引数にとる
    val=reduce(lcm, A)
    ans=0
    MOD=10**9+7
    for i in A:
        ans+=val*pow(i,MOD-2,MOD)%MOD
        ans%=MOD
    print(ans)

    


    
resolve()