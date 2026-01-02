# -*- coding: utf-8 -*-
from heapq import heappush, heapreplace
from itertools import count, product, combinations
from functools import partial, reduce
from math import floor, ceil, sqrt
from collections import defaultdict, deque

def Primes_fnct():
    def b_search(L,t):
        #増大列LについてL[:+1]の要素すべてがt以下であるような最大のi<len(L)を返す。
        search_range = [-1, len(L)]
        update_range = lambda mid: search_range.__setitem__(t<L[mid], mid)
        for _ in [0]*search_range[1].bit_length():
            update_range(sum(search_range)//2)
        return search_range[0]
    
    P = [2,]
    Pappend = P.append
    Q = deque([])
    Qappend = Q.append
    Qpopleft = Q.popleft
    hq = [] 
    integer = count(3,2)
    current_i = 1
    valid_range = 1
    def Primes(*, max_int=None):
        nonlocal valid_range, current_i
        if max_int is None:
            return P[:]

        if  max_int - current_i <= 1:
            return P[:b_search(P,max_int)+1]

        for i in integer:
            if i >= valid_range:
                if Q:
                    q = Qpopleft()
                    heappush(hq, (q**2,q))
                valid_range = Q[0]**2 if Q else i**2

            m,r = hq[0] if hq else (0,0)
            if i != m:
                Pappend(i)
                Qappend(i)

            while m == i:
                heapreplace(hq, (m+2*r, r))
                m,r = hq[0]

            current_i = i
            if max_int - current_i <=1:
                break 
        return P[:]
    return Primes

def factorization(m, Primes=None):
    F = defaultdict(int)
    if m < 2:
        return F

    while not m&1:
        F[2] += 1
        m >>= 1

    if Primes is None:
        Primes = Primes_fnct()

    Primes = deque(Primes(max_int=ceil(sqrt(m))+1))
    Primespopleft = Primes.popleft

    while m > 1 and Primes:
        p = Primespopleft()
        while not m%p:
            m //= p
            F[p] += 1

    if m > 1:
        F[m] += 1
    return F

def solve():
    N = int(input())
    Primes = Primes_fnct()
    F = defaultdict(int)
    for i in range(1,N+1):
        f = factorization(i)
        for k in f.keys():
            F[k] += f[k]
    P = defaultdict(set)
    for k in F.keys():
        for n in (2,4,14,24,74):
            if F[k] >= n:
                P[n] = P[n]|{k,}
    res = 0
    for Q in (((2,1),(4,2)), ((2,1),(24,1)), ((4,1),(14,1)), ((74,1),)):
        R = set()
        if all(len(P[q[0]]) >= q[1] for q in Q):
            for r in product(*(combinations(P[q[0]],q[1]) for q in Q)):
                r_ = [i for j in r for i in j]
                if len(r_) == len(set(r_)):
                    R |= {r,}
        res += len(R)

    return res



if __name__ == '__main__':
    print(solve())