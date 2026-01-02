### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

def yn(b):
    print("Yes" if b==1 else "No")
    return

def bin_search(arr,ls,c):
    l=ls-1
    r = len(arr)
    while (r-l) > 1:
        m = l + (r-l)//2
        if arr[m] >= c:
            r = m
        else:
            l = m
    return l-ls+1

def resolve():
    readline=sys.stdin.readline

    n=int(readline())
    arr=list(map(int, readline().rstrip().split()))
    arr.sort()
    ans=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            c = arr[i] + arr[j]
            ans += bin_search(arr,j+1,c)
    print(ans)
    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------
