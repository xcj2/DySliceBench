# import bisect
from collections import Counter, deque # https://note.nkmk.me/python-scipy-connected-components/
# from copy import copy, deepcopy
# from fractions import gcd
# from functools import reduce
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
#import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def prime_factorize1(N):
        """
        Nをくって、Nの素因数を格納したリストresを返す。
        リストの要素をすべて掛ければNになる"""
        res = []
        x = N
        y = 2
        while y*y <= x:
            while x % y == 0:
                res.append(y)
                x //= y
            y += 1
        if x > 1:
            res.append(x)
        return res

    n=int(input())
    mod=10**9+7
    ans=[]
    for i in range(1,n+1):
        ans.extend(prime_factorize1(i))
    ans=Counter(ans)
    cnt=1
    for j in ans.values():
        cnt*=(j+1)
    print(cnt%mod)





resolve()