
### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest
import os

sys.setrecursionlimit(500*500)

runc=0

def tonari(n,x,keta,k):
    #print(n,end="")
    #print(" ",end="")
    #print(x,end="")
    #print(" ",end="")
    #print(keta)
    global runc
    if keta==1:
        runc+=1
        if runc==k:
            print(n)
            sys.exit()
        return 0

    if x==0:
        yy=[0,1]
    elif x==9:
        yy=[8,9]
    else:
        yy=[x-1,x,x+1]
    for y in yy:
        #rint(y)
        tonari(n+y*(10**(keta-2)),y,keta-1,k)
        #if res!=0:
        #    return res

    

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline
    k=int(readline())

    for keta in range(1,100):
        for i in range(1,10):
            tonari(i*(10**(keta-1)),i,keta,k)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------