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
    N, A, B = LI()
    S = SI()
    d = defaultdict(int)
    for s in S:
        if s=="a":
            if d["a"]+d["b"]<A+B:
                print("Yes")
                d[s] += 1
            else:
                print("No")
        elif s=="b":
            if d["a"]+d["b"]<A+B and d["b"]<B:
                print("Yes")
                d[s] += 1
            else:
                print("No")
        else:
            print("No")
    return

def examC():
    W, H = LI()
    P = [I() for _ in range(W)]; P.sort()
    Q = [I() for _ in range(H)]; Q.sort()
    dh = 0; dw = 0
    p = 0; q = 0
    ans = 0
    for i in range(H+W):
        if (q<H and p<W and P[p]<Q[q]) or not q<H:
            ans += P[p]*(H+1-dh)
            p +=1; dw +=1
        else:
            ans += Q[q]*(W+1-dw)
            q +=1; dh+=1
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
global mod,mod2,inf,alphabet,ALPHABET, _ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 1e-9
alphabet = [chr(ord('a') + i) for i in range(26)]
ALPHABET = [chr(ord('A') + i) for i in range(26)]

if __name__ == '__main__':
    examC()
