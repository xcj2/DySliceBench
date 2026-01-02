from collections import defaultdict
from collections import deque
from string import ascii_uppercase
import sys, bisect, math, heapq

stdin = sys.stdin
read_int = lambda : list(map(int,stdin.readline().split()))

A, B, C, D = read_int()

def lcm(a, b):
    pa, pb = a, b
    if a > b:
        a, b = b, a
    while b % a != 0:
        a, b = b % a, a
    return pa * pb // a

def divi(a, b, m):
    ans = 0
    former = a // m
    latter = b // m
    ans = latter - former
    if a % m == 0:
        ans += 1
    return ans

def solve():
    return (B - A + 1) - (divi(A, B, C) + divi(A, B, D) - divi(A, B, lcm(C, D)))

if __name__ == "__main__":
    print(solve())