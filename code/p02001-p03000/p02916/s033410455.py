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
B = III()
C = III()

ans = 0
for i in range(N):
    ans += B[i]
    if i!=N-1:
        if A[i+1] == A[i]+1:
            ans += C[A[i]-1]
        
print(ans)