def examA():
    S = SI(); N = len(S)
    T = "CODEFESTIVAL2016"
    ans = 0
    for i in range(N):
        if S[i]!=T[i]:
            ans +=1
    print(ans)
    return

def examB():
    return

def examC():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,ALPHABET, _ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 1e-9
alphabet = [chr(ord('a') + i) for i in range(26)]
ALPHABET = [chr(ord('A') + i) for i in range(26)]

if __name__ == '__main__':
    examA()
