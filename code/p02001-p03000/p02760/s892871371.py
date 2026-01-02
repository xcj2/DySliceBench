import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import copy

sys.setrecursionlimit(10**9)
mod = 10**7+9
inf = 10**20

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

a = []
for i in range(3):
    a.append(LI())

ll = [[0]*3 for i in range(3)]

n = I()
for i in range(n):
    b = I()
    for j in range(3):
        for k in range(3):
            if a[j][k]==b:
                ll[j][k]=1

for i in range(3):
    if ll[i]==[1,1,1]:
        print("Yes")
        exit()
for i in range(3):
    if ll[0][i]==1 and ll[1][i]==1 and ll[2][i]==1:
        print("Yes")
        exit()

if ll[0][0]==1 and ll[1][1]==1 and ll[2][2]==1:
    print("Yes")
    exit()
if ll[0][2]==1 and ll[1][1]==1 and ll[2][0]==1:
    print("Yes")
    exit()

print("No")