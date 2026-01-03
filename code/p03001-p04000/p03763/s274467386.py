def examC():
    N = I()
    d = defaultdict(int)
    for i in range(N):
        curD = defaultdict(int)
        S = SI()
        for s in S:
            curD[s]+=1
        if i==0:
            d = curD
            continue
        for s in alphabet:
            d[s] = min(d[s],curD[s])
    d = sorted(d.items())
    ans = ""
    for key,i in d:
        ans +=key*i
    print(ans)
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
    examC()
