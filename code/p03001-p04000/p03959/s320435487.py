import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()
T = LI()
A = LI()

if T[0] > A[0]:
    print(0)
    exit()

if T[N-1] < A[N-1]:
    print(0)
    exit()

ans = 1
for i in range(1,N-1):
    if T[i-1] != T[i]:
        if A[i] < T[i]:
            print(0)
            exit()
        else:
            continue
    else:
        if A[i+1] != A[i]:
            if T[i] < A[i]:
                print(0)
                exit()
            else:
                continue
        else:
            ans *= min(A[i],T[i])
            ans %= mod

print(ans)