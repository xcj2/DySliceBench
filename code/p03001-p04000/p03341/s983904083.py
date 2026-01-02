def examC():
    N = I()
    S = SI()
    E = S.count("E"); W = N-E
    curW = 0; curE = 0
    ans = N-1
    for i in range(N):
        if S[i]=="W":
            curW +=1
        cur = N -1 - (W-curW) - curE
        if S[i]=="E":
            curE +=1
        ans = min(ans,cur)
#        print(cur)
    print(ans)
    return

def examD():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,ALPHABET
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]
ALPHABET = [chr(ord('A') + i) for i in range(26)]

if __name__ == '__main__':
    examC()
