import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

MOD = 10**9 + 7

# 右側に自身より低い数値をいくつ残せているか

N,*A = map(int,read().split())

A_rev = A[::-1]

class BIT():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        
    def get_sum(self,i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i

right_zero = [0] * (N+1)
for i,x in enumerate(A_rev):
    right_zero[i+1] = right_zero[i] 
    if x == 0:
        right_zero[i+1] += 1

zero_cnt = right_zero[-1]
inv = pow(zero_cnt,MOD-2,MOD)

rest_smaller = [1] * (N+1)
for x in A:
    rest_smaller[x] = 0
rest_smaller = list(itertools.accumulate(rest_smaller))

right_smaller_prob = [(MOD+1)//2] * N
for i,x in enumerate(A_rev):
    if x != 0:
        right_smaller_prob[i] = rest_smaller[x] * inv

right_smaller_filled = [0] * N
bit = BIT(max_n = N)
p = 0
for i,x in enumerate(A_rev):
    if x != 0:
        right_smaller_filled[i] = bit.get_sum(x)
        bit.add(x,1)
        p += zero_cnt-rest_smaller[x]
    else:
        right_smaller_filled[i] = p * inv

fact = [1] * (N+1)
for n in range(1,N+1):
    fact[n] = fact[n-1] * n % MOD

answer = (1+sum(y*(x*p+z) for x,p,y,z in zip(right_zero,right_smaller_prob,fact,right_smaller_filled))) * fact[zero_cnt] % MOD
print(answer)