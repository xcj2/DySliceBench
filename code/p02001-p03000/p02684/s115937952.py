# coding: utf-8

import sys
import math
import collections
import itertools
import bisect
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return x if y == 0 else gcd(y, x%y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def LS() : return input().split()
def RS(N) : return [input() for _ in range(N)]
def LRS(N) : return [input().split() for _ in range(N)]
def PL(L) : print(*L, sep="\n")
def YesNo(B) : print("Yes" if B else "No")
def YESNO(B) : print("YES" if B else "NO")

N, K = LI()
A = LI()

tel = [-1] * N
flag = True
i = 0
time = 1
while True:
    # print(i, end=" ")
    if time == K:
        print(A[i])
        flag = False
        break
    
    if tel[i] == -1:
        tel[i] = [time, A[i]-1]
        i = A[i]-1
    else:
        # i = A[i]-1
        break
        # pass
    
    time += 1
    # print(time, tel)
# print()
# print(time-1)
# print(time - tel[i][0])
# print((K - (time-1)) % (time - tel[i][0]))

if flag:
    for _ in range((K - (time-1)) % (time - tel[i][0])):
        i = A[i]-1

    print(i+1)
