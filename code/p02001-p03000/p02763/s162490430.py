from sys import stdin
import sys
#import numpy as np
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

class fenwick_tree:
    def __init__(self, n):
        self.N = n
        self.n = 1 # pow of 2
        while(self.n < self.N):
            self.n *= 2
        self.data = [0] * (self.n + 1)

    def add(self, idx, x):
        while idx <= self.n:
            self.data[idx] += x
            idx += (idx & -idx)

    def cumulate(self, idx):
        s = 0
        while idx > 0:
            s += self.data[idx]
            idx -= (idx & -idx)
        return s

def main():
    N = ri()
    S = rs()
    Q = ri()
    ans = []

    bit = [fenwick_tree(N) for i in range(26)]
    for i in range(N):
        d = ord(S[i]) - ord('a')
        bit[d].add(i + 1, 1)

    ca = [c for c in S]
    for _ in range(Q):
        ss = rsa()
        if ss[0] == '1':
            pos = int(ss[1]) - 1
            c = ss[2][0]
            bit[ord(ca[pos]) - ord('a')].add(pos + 1, -1)
            ca[pos] = c
            bit[ord(ca[pos]) - ord('a')].add(pos + 1, +1)
        else:
            l = int(ss[1]) - 1
            r = int(ss[2]) - 1
            cnt = 0
            for i in range(26):
                su = bit[i].cumulate(r + 1) - bit[i].cumulate(l)
                if su > 0: cnt += 1
            ans.append(cnt)
    
    print("\n".join([str(n) for n in ans]))


if __name__ == "__main__":
    main()
