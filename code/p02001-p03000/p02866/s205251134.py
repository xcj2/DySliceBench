#!/usr/bin/env python3
import sys

#lines = stdin.readlines()
def rint():
    return map(int, sys.stdin.readline().split())

def input():
    return sys.stdin.readline().rstrip('\n')

def oint():
    return int(input())

N = oint()

d = list(rint())

if d[0] != 0:
    print(0)
    exit()

d.sort()

if N > 1 and d[1] == 0:
    print(0)
    exit()

n = 1
c = 0
cprev = 1
ans = 1
for i in range(1, N):
    if d[i] == n:
        c+=1
    elif d[i] != n+1:
        print(0)
        exit()
    else:
        ans = (ans* pow(cprev, c, 998244353))%998244353
        n += 1
        cprev = c
        c = 1

ans = (ans* pow(cprev, c, 998244353))%998244353
print(ans)


