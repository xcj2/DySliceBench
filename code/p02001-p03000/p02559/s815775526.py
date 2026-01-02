# Date [ 2020-09-08 00:04:04 ]
# Problem [ b.py ]
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

class BinaryIndexedTree:
    def __init__(self, n):
        '''1-index'''
        self.size = n + 1
        self.data = [0] * self.size
        self.element = [0] * self.size
        self.depth = 1 << n.bit_length() - 1
    
    def build(self, array):
        for i, x in enumerate(array):
            self.add(i, x)

    def add(self, i, v):
        self.element[i] += v; i += 1 # 1-index
        while i < self.size:
            self.data[i] += v
            i += i & -i
    
    def sum(self, i):
        ret = 0; i += 1 # 1-index
        while i > 0:
            ret += self.data[i]
            i -= i & -i
        return ret
    
    def query(self, l, r=None):
        '''get sum [l, r)'''
        if r == None: return self.element[l]
        return self.sum(r) - self.sum(l-1)

    def lower_bound(self, v):
        if v <= 0: return 0
        k = self.depth; i = 0
        while k > 0:
            if i+k < self.size and self.data[i+k] < v:
                v -= self.data[i+k]
                i += k
            k >>= 1
        return i + 1
    
    def upper_bound(self, v):
        if v <= 0: return 0
        k = self.depth; i = 0
        while k > 0:
            if i+k < self.size and self.data[i+k] <= v:
                v -= self.data[i+k]
                i += k
            k >>= 1
        return i + 1

def Main():
    n, q = read_ints()
    bit = BinaryIndexedTree(n)
    a = read_int_list()
    bit.build(a)
    for _ in range(q):
        t, l, r = read_ints()
        if t == 0:
            bit.add(l, r)
        else:
            print(bit.query(l, ~-r))    

if __name__ == '__main__':
    Main()
