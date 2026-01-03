def examA():
    S = SI()
    if "W" in S and not "E" in S:
        print("No")
    elif "E" in S and not "W" in S:
        print("No")
    elif "N" in S and not "S" in S:
        print("No")
    elif "S" in S and not "N" in S:
        print("No")
    else:
        print("Yes")
    return

def examB():
    N = I()
    A = [I()for _ in range(N)]
    ans = 0
    for i in range(N-1):
        ans += A[i]//2
        if A[i]%2 and A[i+1]>=1:
            ans += 1
            A[i+1] -= 1
    ans += A[N-1]//2
    print(ans)
    return

def examC():
    N = I()
    A = [I()for _ in range(N)]
    if N==1:
        print(0)
        return
    odd = set()
    for i in range(N):
        if i&1==0:
            odd.add(A[i])
    A.sort()
    ans = 0
    for i in range((N+1)//2):
        if A[i*2] in odd:
            continue
        ans += 1
    print(ans)
    return

def examD():
    def factorization_(a):
        rep = [[]for _ in range(2)]
        pair = []
        for i in range(2,int(10**(3.4))+2):
            cur = 0
            while a%i==0:
                cur += 1
                a //= i
            if cur>0:
                cur %= 3
                if cur==0:
                    continue
                rep[0].append((i,cur))
                pair.append((i,3-cur))
        if not rep[0]:
            rep[0].append((0,0))
            pair.append((0,0))
        rep[1] = a
        rep[0] = tuple(rep[0])

        rep = tuple(rep)
        pair = tuple(pair)
        return rep, pair

    def square(a):
        rep = set()
        for i in range(int(10**(3.3)),a+1):
            rep.add(i**2)
        return rep

    N = I()
    S = [I()for _ in range(N)]
    group = defaultdict(int)
    P = defaultdict(tuple)
    for s in S:
        g,p = factorization_(s)
        group[g] += 1
        P[g[0]] = p
    #print(group)
    #G2 = deepcopy(group)
    #print(P)
    sq = square(int(10**(5))+1)
    ans = 0
    for key,c in group.items():
        rep, rest = key
        if rest in sq:
            pair = int(pow((rest+1),0.5))
        else:
            pair = rest**2
        if rep==((0,0),) and pair==1:
            ans += 1
        else:
            if (P[rep],pair) in group:
                if c < group[(P[rep], pair)]:
                    ans += group[(P[rep], pair)]
                else:
                    ans += c
                group[(P[rep], pair)] = 0
            else:
                ans += c
            group[key] = 0
        #print(ans)
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examD()

"""

"""
