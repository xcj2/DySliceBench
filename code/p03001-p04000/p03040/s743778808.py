import sys
input = sys.stdin.readline
from collections import defaultdict

def compress(l):
    l = list(set(l))
    l.sort()
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    
    for i in range(len(l)):
        d1[l[i]] = i
        d2[i] = l[i]
    
    return d1, d2

class BIT:#0-indexed
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    
    def acc(self, i):#a0+...+ai
        i += 1
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s
    
    def add(self, i, x):#ai += x
        i += 1
        
        while i<=self.n:
            self.bit[i] += x
            i += i&(-i)

def binary_search(c):
    l, r = 0, L-1
    
    while l<=r:
        m = (l+r)//2
        
        if bit.acc(m)>=(c+1)//2:
            r = m-1
        else:
            l = m+1
    
    return l
    
Q = int(input())
que = []
l = []

for _ in range(Q):
    que_i = tuple(map(int, input().split()))
    
    if len(que_i)==3:
        l.append(que_i[1])
    
    que.append(que_i)

d1, d2 = compress(l)
L = len(list(d1.keys()))
bit = BIT(L)
bit2 = BIT(L)
cnt = 0
b_acc = 0

for que_i in que:
    if len(que_i)==3:
        a, b = que_i[1], que_i[2]
        bit.add(d1[a], 1)
        bit2.add(d1[a], a)
        b_acc += b
        cnt += 1
    else:
        med_idx = binary_search(cnt)
        med = d2[med_idx]
        s = bit.acc(med_idx)*med-bit2.acc(med_idx)+(bit2.acc(L-1)-bit2.acc(med_idx))-(bit.acc(L-1)-bit.acc(med_idx))*med
        s += b_acc
        print(med, s)