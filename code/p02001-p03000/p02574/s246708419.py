# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

class factorials:
    '''
    args:
      n : max val when exploring factorials
    '''
    def __init__(self, n):
        self.n = 1# factorials to be searched
        self.factorials = set()
        self.update_factorials(n)

    def update_factorials(self, n):
        if self.n >= n:
            return None
        for i in range(self.n+1, n+1):
            done = False
            limit = int(i ** 0.5)
            for j in self.factorials:
                if j > limit: break
                if not i % j:
                    done = True
                    break
            if not done:
                self.factorials.add(i)
        self.n = n
        return None

    def factorials_set(self):
        return self.factorials

    def check_fact(self, x):
        if x > self.n**2:
            self.update_factorials(int(x ** 0.5)+1)
        MAX = int(math.sqrt(x))
        for f in self.factorials:
            if f > MAX:break
            if not x % f:
                return False
        return True

    def prime_factorization(self, val, divisors=None):
        # divisors : default-dict of divisors. Should be specified only if appended vals are required
        max_n = int(math.sqrt(val))
        if self.n < max_n:
            self.update_factorials(max_n)
        if divisors == None:
            divisors = defaultdict(lambda: 0)
        for f in self.factorials:
            if f > val: break
            while True:
                if not val % f:
                    divisors[f] += 1
                    val //= f
                else:
                    break
        if val > 1:
            divisors[val] += 1
        return divisors

def run():
    N, *A = map(int, read().split())
    MAX = max(A)
    nn = int(MAX ** 0.5)
    FACT = factorials(nn)
    FACT_SET = FACT.factorials_set()
    #print(FACT_SET)
    fact_get = set()
    done = False
    for a in A:
        #print(a, fact_get)
        if done: break
        for f in FACT_SET:
            if not a % f:
                if f in fact_get:
                    done = True
                    break
                fact_get.add(f)
                while not a % f:
                    a //= f
        if a > 1:
            if a in fact_get:
                done = True
                break
            fact_get.add(a)
    if not done:
        print('pairwise coprime')
        return

    SETWISE = False
    setwise_fact = set()
    mina = min(A)
    for f in FACT_SET:
        if not mina % f:
            setwise_fact.add(f)
            while not mina % f:
                mina //= f
    if mina > 1:
        setwise_fact.add(mina)

    for a in A:
        remlist = []
        if len(setwise_fact) == 0:
            print('setwise coprime')
            return
        for f in setwise_fact:
            if not a % f:
                continue
            else:
                remlist.append(f)
        for f in remlist:
            setwise_fact.remove(f)
        #print(a, setwise_fact)
    if len(setwise_fact) == 0:
        print('setwise coprime')
        return


    print('not coprime')



if __name__ == "__main__":
    run()