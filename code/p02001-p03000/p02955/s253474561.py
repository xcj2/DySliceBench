# -*- coding: utf-8 -*-

from heapq import heappush, heapreplace
from itertools import count, product
from functools import reduce
from math import ceil, sqrt
from collections import defaultdict, deque

class Primes_C(object):
    def b_search(L,t):
        #増大列LについてL[:+1]の要素すべてがt以下であるような最大のi<len(L)を返す。
        search_range = [-1, len(L)]
        update_range = lambda mid: search_range.__setitem__(t<L[mid], mid)
        for _ in range(search_range[1].bit_length()):
            update_range(sum(search_range)//2)
        return search_range[0]
    
    def __init__(self):
        self.P = [2]
        self.Pappend = self.P.append
        self.Q = deque([])
        self.Qappend = self.Q.append
        self.Qpopleft = self.Q.popleft
        self.hq = [] 
        self.integer = count(3,2)
        self.current_i = 2
        self.valid_range = 1
        self.iter_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_index >= len(self.P):
            self.step_calc(1)
        self.iter_index += 1
        return self.P[self.iter_index-1]
        pass

    def iter_reset(self, index=0):
        self.iter_index = index

    def list(self, max_int=None):
        if max_int is None:
            return self.P[:]

        if  max_int <= self.current_i:
            return self.P[:Primes_C.b_search(self.P,max_int)+1]

        else:
            self.calc(max_int)
            return self.P[:]

    def extend(self, i):
        if i >= self.valid_range:
            if self.Q:
                q = self.Qpopleft()
                heappush(self.hq, (q**2,q))
            self.valid_range = self.Q[0]**2 if self.Q else i**2

    def check_update(self,i):
        m,r = self.hq[0] if self.hq else (0,0)
        flag =  (i != m)
        if flag:
            self.Pappend(i)
            self.Qappend(i)
        while m == i:
            heapreplace(self.hq, (m+2*r, r))
            m,r = self.hq[0]
        return flag

    def calc(self, max_int):
        for i in self.integer:
            self.extend(i)
            self.check_update(i) 
            self.current_i = i+1
            if max_int <= self.current_i:
                break

    def step_calc(self, step):
        for i in self.integer:
            self.extend(i)
            step -= self.check_update(i) 
            self.current_i = i+1
            if not step:
                break

    def factorization(self, m, F=defaultdict(int)):
        max_int = ceil(sqrt(max(m, 0)))
        index0 = len(self.P)
        index = 0
        p = self.P[0]
        while m > 1 and p <= max_int:
            while not m%p:
                m //= p
                F[p] += 1

            index += 1
            if index >= index0:
                self.step_calc(1)
            p = self.P[index]

        if m > 1:
            F[m] += 1

        return F



def solve():
    N, K = map(int, input().split())
    A = tuple(map(int, input().split()))
    Primes = Primes_C()

    F = Primes.factorization(sum(A))
    res = 1
    for q in product(*[[p**m for m in range(F[p]+1)] for p in F]):
        d = reduce(int.__mul__, q)
        B = sorted([a%d for a in A])
        if sum(B)-sum(B[-(sum(B)//d):]) <= K:
            res = max(res, d)

    return str(res)

if __name__ == '__main__':
    print(solve())