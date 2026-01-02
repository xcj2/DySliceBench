import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

import itertools
import math

n = I()
p = LI()
q = LI()
nums = range(1,n+1)

count = 0
for lis in itertools.permutations(nums,n):
    pflg = True
    qflg = True
    for i in range(n):
        if(p[i] != lis[i]):
            pflg = False
        if(q[i] != lis[i]):
            qflg = False
    if(pflg):
        a = count
    if(qflg):
        b = count
    count += 1

print(abs(b-a))