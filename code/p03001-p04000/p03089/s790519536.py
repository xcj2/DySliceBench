from collections import deque
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
l = IL()

ans = []
while l:
    for i in range(N-1,-1,-1):
        if l[i] == i+1:
            num = l.pop(i)
            ans.append(num)
            N -= 1
            break
    else:
        print(-1)
        exit()

for i in range(len(ans)-1,-1,-1):
    print(ans[i])