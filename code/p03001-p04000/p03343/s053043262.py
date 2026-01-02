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
    N = I()
    A = LI()
    cur = [0]*21
    k = 0; ans = 0
    flag = True
    for i in range(N):
        for j in range(21):
            if cur[j]>=2:
                a = A[i]
                for l in range(21):
                    if a & (1 << l) == (1 << l):
                        cur[l] -= 1
                continue
        flag = True
        while(k<N):
            a = A[k]
            for j in range(21):
                if a&(1<<j)==(1<<j):
                    if cur[j]>=1:
                        flag = False
                        break
            if flag:
                for j in range(21):
                    if a & (1 << j) == (1 << j):
                        cur[j] += 1
                k +=1
            if not flag:
                break
        ans += k-i
#        print(i,k,ans,cur)
        a = A[i]
        for j in range(21):
            if a & (1 << j) == (1 << j):
                cur[j] -= 1

    print(ans)
    return

def examE():
    N, K, Q = LI()
    A = LI()
    ans = inf
    for i in range(N):
        a = A[i]
        curL = []
        l = 0; r = 0
        while(l<N):
            while(r<N):
                if A[r]<a:
                    break
                r +=1
            if l<r:
                curL.append(A[l:r])
            l = r+1
            r = l
#        print(curL)
        cur = []
        for v in curL:
            if len(v)>=K:
                v.sort()
                for j in range(len(v)-K+1):
                    cur.append(v[j])
#        print(cur)
        if len(cur)>=Q:
            cur.sort()
            now = cur[Q-1]-cur[0]
            ans = min(ans,now)
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
global mod,mod2,inf,alphabet,ALPHABET
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]
ALPHABET = [chr(ord('A') + i) for i in range(26)]

if __name__ == '__main__':
    examE()
