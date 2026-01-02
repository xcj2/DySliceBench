import bisect
from operator import itemgetter
import math
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,sunke,hunke,Gs,Gh = IL()
s = S()

f = 0
for i in range(sunke-1,max(Gs,Gh)):
    if f == 0:
        if s[i]=="#":
            f = 1
    else:
        if s[i]=="#":
            print("No")
            exit()
        else:
            f = 0

cnt = 0
cntf = 0
for i in range(hunke-2,min(Gs,Gh)+1):
    if s[i]=="#":
        cnt = 0
    else:
        cnt += 1
    if cnt == 3:
        cntf = 1
        break

if (sunke < hunke) and (Gs > Gh):
    if cntf == 1:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")