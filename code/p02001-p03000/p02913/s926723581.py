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

def z_algorithm(s: list):
    n = len(s)
    if n == 0: return []
    z = [-1] * n
    z[0] = 0; j = 0
    for i in range(1, n):
        k = z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + k < n and s[k] == s[i + k]: k += 1
        z[i] = k
        if j + z[j] < i + z[i]: j = i
    z[0] = n
    return z

def z_algorithm2(s: str):
    n = len(s)
    s2 = list(map(ord, s))
    return z_algorithm(s2)

def Main():
    n = read_int()
    s = read_str()
    ans = 0
    for i in range(n):
        lcp = z_algorithm2(s[i:])
        for j, x in enumerate(lcp):
            ans = max(ans, min(j, x))
    print(ans)

if __name__ == '__main__':
    Main()