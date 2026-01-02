def examA():
    R = I()
    if R<1200:
        ans = "ABC"
    elif R<2800:
        ans = "ARC"
    else:
        ans = "AGC"
    print(ans)
    return

def examB():
    S = SI(); N = len(S)
    ans = "AC"
    if not S[0]=="A":
        ans = "WA"
    flag = False
    for i in range(2,N-1):
        if S[i]=="C":
            flag = True
    if not flag:
        ans = "WA"
    num = 0
    for i in S:
        if ord("A")<=ord(i)<=ord('Z'):
            num +=1
    if not num==2:
        ans = "WA"
    print(ans)
    return

def examC():
    return

def examD():
    return

def examE():
    return

def examF():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()
