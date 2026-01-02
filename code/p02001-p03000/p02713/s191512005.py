### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline

    #n,m,k=map(int, readline().rstrip().split())
    #arr=list(map(int, readline().rstrip().split()))
    k=int(readline())
    #ss=readline().rstrip()
    #yn(1)
    ans=0
    for a in range(1,k+1):
        for b in range(1,k+1):
            for c in range(1,k+1):
                ans+=gcd(a,b,c)
    print(ans)



    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------
