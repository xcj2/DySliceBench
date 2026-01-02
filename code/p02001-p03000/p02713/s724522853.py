import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

import math # version 3.4
from collections import defaultdict
from functools import reduce

from itertools import product
k = n_in()
#k = 200

memo = {}

def gcd(a,b):
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    if b < a:
        a,b = b,a
    if (a,b) in memo:
        return memo[(a,b)]
    else:
        memo[(a,b)] = math.gcd(a,b)
        return memo[(a,b)]
    
res = 0
for a,b,c in product(range(1,k+1), repeat=3):
    q = gcd(a,b)
    res += gcd(q,c)

print(res)
