# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
from _collections import defaultdict
from functools import lru_cache

class cin():
    def int():
        return int(sys.stdin.readline().rstrip())
    def string():
        return sys.stdin.readline().rstrip()
    def mapInt():
        return [int(x) for x in cin.string().split()]
    def stringList(n):
        return [input() for i in range(n)]
    def intListList(n):
        return [cin.mapInt() for i in range(n)]
    def intColsList(n):
        return [int(input()) for i in range(n)]
        
class Math():
    def gcd(a,b):
        if b == 0:
            return a
        return Math.gcd(b,a % b)
    def lcm(a,b):
        return (a * b) // Math.gcd(a,b)
    def roundUp(a,b):
        return -(-a // b)
    def toUpperMultiple(a,x):
        return Math.roundUp(a,x) * x
    def toLowerMultiple(a,x):
        return (a // x) * x
    def nearPow2(n):
        if n <= 0:
            return 0
        if n & (n - 1) == 0:
            return n
        ret = 1
        while(n > 0):
            ret <<= 1
            n >>= 1
        return ret
    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3,d + 1,2):
            if n % i == 0:
                return False
        return True

def fact(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2,Math.roundUp(int(n ** 0.5),1) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt+=1
                temp //= i
            arr[i] = cnt
    if temp != 1:
        arr[temp] = 1
    if arr == []:
        arr[n] = 1
    return arr
MOD = int(1e09) + 7

def main():
    N = cin.int()
    S = defaultdict(int)
    for i  in range(1,N + 1):
        T = fact(i)
        for k,v in T.items():
            S[k] += v
    ans = 1
    for v in S.values():
        ans *= (v+1)
        ans %= MOD
    print(ans)
    return

if __name__ == "__main__":
    main()
