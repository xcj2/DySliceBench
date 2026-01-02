class fenwick_tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    
    def add(self, p: int, x: int):
        assert 0 <= p and p <= self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    
    def sum(self, l: int, r: int) -> int:
        assert 0 <= l and l <= r and r <= self._n
        return self.__sum(r) - self.__sum(l)
    
    def __sum(self, r: int) -> int:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

# Date [ 2020-09-11 22:06:11 ]
# Problem [ fenwicktree.py ]
# Author Koki_tkg

import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_ints2(x):   return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a%b==0 else GCD(b, a%b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)

def Main():
    n, q = read_ints()
    a = read_int_list()
    fw = fenwick_tree(n)
    for i, x in enumerate(a):
        fw.add(i, x)
    for _ in range(q):
        query = read_int_list()
        if query[0] == 0:
            fw.add(query[1], query[2])
        else:
            print(fw.sum(query[1], query[2]))

if __name__ == '__main__':
    Main()