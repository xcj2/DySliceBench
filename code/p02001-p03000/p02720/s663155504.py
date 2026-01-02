# coding: utf-8

import sys
import math
import collections
import itertools
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def PL(L) : print(*L, sep="\n")

K = I()

stack = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
ok = [[0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9], [8,9]]

i = 0
while len(stack) < K:
    p = stack[i]
    tm = ok[p[-1]]
    
    for t in tm:
        stack.append(p+[t])
    
    i += 1

# print(stack)

for i in stack[K-1]:
    print(i, end="")
print()
