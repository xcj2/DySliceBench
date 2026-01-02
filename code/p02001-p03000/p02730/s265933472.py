### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

def yn(b):
    print("Yes" if b==1 else "No")
    return

def kaibun(s):
    l=len(s)
    for i in range(l//2):
        if s[i]!=s[-1*(i+1)]:
            return False
    return True

def resolve():
    readline=sys.stdin.readline

    #n,m,k=map(int, readline().rstrip().split())
    #arr=list(map(int, readline().rstrip().split()))
    #n=int(readline())
    ss=readline().rstrip()
    #yn(1)
    n=len(ss)
    yn(kaibun(ss) and kaibun(ss[0:(n-1)//2]) and kaibun(ss[(n+3)//2-1:n]))

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------