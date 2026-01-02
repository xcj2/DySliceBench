def examA():
    C = [SI()for _ in range(3)]
    ans = C[0][0]+C[1][1]+C[2][2]
    print(ans)
    return

def examB():
    N, M = LI()
    P = [0]*N
    S = [LSI()for _ in range(M)]
    pena = 0
    ac = set()
    for p,s in S:
        p = int(p)-1
        if s=="WA":
            P[p] += 1
        else:
            if p in ac:
                continue
            ac.add(p)
            pena += P[p]

    print(len(ac),pena)
    return

def examC():
    W, H, N = LI()
    lx, rx, ly, ry = 0, W, 0, H
    A = [LI()for _ in range(N)]
    for x,y,a in A:
        if a==1:
            lx = max(lx,x)
        elif a==2:
            rx = min(rx,x)
        elif a==3:
            ly = max(ly,y)
        elif a==4:
            ry = min(ry,y)
    ans = max(0,rx-lx)*max(0,ry-ly)
    print(ans)
    return

def examD():
    N, H = LI()
    B = [0]*N
    maxa = 0
    ans = 0
    for i in range(N):
        a, B[i] = LI()
        if a>maxa:
            maxa = a
    B.sort(reverse=True)
    for b in B:
        if b<maxa:
            break
        H -= b
        ans += 1
        if H<=0:
            print(ans)
            return
    ans += -(-H//maxa)
    print(ans)
    return

def examE():
    A, B = LI()
    ans = [["#"]*100 for _ in range(50)] + [["."]*100 for _ in range(50)]
    i = 0; j = 0
    for _ in range(A-1):
        ans[i][j] = "."
        j += 2
        if j>=100:
            j = 0; i += 2
    i = 0; j = 0
    for _ in range(B-1):
        ans[99-i][j] = "#"
        j += 2
        if j>=100:
            j = 0; i += 2
    print(100,100)
    for v in ans:
        print("".join(map(str,v)))
    return

def examF():
    def search_1(need):
        l = 0; r = inf+1
        while(r-l)>1:
            now = (l+r)//2
            cur = 0
            cur += shakutori(neg,pos,now)
            #print(cur,now)
            if cur>=need:
                l = now
            else:
                r = now
            #print(cur)
        return -l
    def search_2(need):
        need *= 2
        #print(need)
        l = 0; r = inf
        while(r-l)>1:
            now = (l+r)//2
            cur = 0
            cur += shakutori_2(neg,now)
            cur += shakutori_2(pos,now)
            if cur>=need:
                r = now
            else:
                l = now
            #print(cur,now)
        return r
    def shakutori(A,B,k):
        n = len(A)
        m = len(B)
        rep = 0
        r = 0
        for l in range(n)[::-1]:
            while(r<m-1 and A[l]*B[r]<k):
                r += 1
            if (A[l]*B[r]>=k):
                rep += m-r
        return rep
    def shakutori_2(C,k):
        n = len(C)
        rep = 0
        r = n-1
        for l in range(n):
            while(r>0 and C[l]*C[r]>k):
                r -= 1
            if (C[l]*C[r]<=k):
                rep += r+1
                if r >= l:
                    rep -= 1
        return rep
    N, K = LI()
    A = LI()
    neg = []; pos = []; arr_0 = 0
    for a in A:
        if a<0:
            neg.append(-a)
        elif a==0:
            arr_0 += 1
        else:
            pos.append(a)
    neg.sort(); pos.sort()
    #print(pos)
    if len(neg)*len(pos)>=K:
        ans = search_1(K)
    elif len(neg)*len(pos)+arr_0*(len(neg)+len(pos))+arr_0*(arr_0-1)//2>=K:
        ans = 0
    else:
        ans = search_2(K-len(neg)*len(pos)-arr_0*(len(neg)+len(pos))-arr_0*(arr_0-1)//2)
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
87940638538504699
448283280358331064
"""