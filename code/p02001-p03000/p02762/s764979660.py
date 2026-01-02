from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq

##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##

class union_find:
    def __init__(self, n):
        self.N = n
        self._parent = [i for i in range(self.N)]
        self._mem = [1] * self.N
        self.compo = self.N

    def parent(self, a):
        if self._parent[a] == a:
            return a
        self._parent[a] = self.parent(self._parent[a])
        return self._parent[a]

    def united(self,a, b):
        return self.parent(a) == self.parent(b)
    
    def unite(self,a, b):
        a = self.parent(a)
        b = self.parent(b)
        if(a == b): return False
        if self._mem[a] > self._mem[b]: a, b = b, a
        self._parent[a] = b
        self._mem[b] += self._mem[a]
        self.compo -= 1
        return True
    
    def is_root(self,a):
        return a == self._parent[a]
    def mem_cnt(self,a):
        return self._mem[self.parent(a)]
    def dump(self):
        print(self._parent)
    

def main():
    N, M, K = rip()
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = rip()
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = rip()

    uf = union_find(N)
    for i in range(M):
        uf.unite(A[i] - 1, B[i] - 1)

    ans = [0] * N
    for i in range(N):
        ans[i] = uf.mem_cnt(i) - 1
    for i in range(K):
        if uf.united(C[i] - 1, D[i] - 1):
            ans[C[i] - 1] -= 1
            ans[D[i] - 1] -= 1
    for i in range(M):
        ans[A[i] - 1] -= 1
        ans[B[i] - 1] -= 1

    print(" ".join([str(n) for n in ans]))

if __name__ == "__main__":
    main()
