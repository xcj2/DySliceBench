import collections
import itertools
import numpy as np
import sys
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def gcd(a,b):
    while b % a:
        a,b = b, a % b
    return a

N,K = IL()

if N == 1:
    if K == I():
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
else:
    l = IL()
    l.sort(reverse=True)

    if K <= l[0]:
        num = gcd(l[0],l[1])
        for i in l:
            if i%num == 0:
                continue
            else:
                num = gcd(num,i)
        if K%num == 0:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
    else:
        print("IMPOSSIBLE")