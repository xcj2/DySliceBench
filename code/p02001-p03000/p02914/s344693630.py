import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N = I()
A = III()

xor = 0
for i in range(N):
    xor ^= A[i]

for i in range(N):
    A[i] &= ~xor

max_digit = len(format(max(A), 'b'))
rank = 0
for col in range(max_digit)[::-1]:
    pivot = -1
    for row in range(rank,N):
        if A[row]>>col & 1:
            pivot = row
            break
    if pivot == -1: 
        continue
    A[pivot],A[rank] = A[rank],A[pivot]
    for row in range(rank+1,N):
        if A[row]>>col & 1:
            A[row] ^= A[rank]
    rank += 1

val = 0
for i in range(N):
    val = max(val,val^A[i])

print(2*val + xor)