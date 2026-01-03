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
s = str(input())

# 0:羊  1:狼
a = [-1]*N
A1,A2,A3,A4 = a[:],a[:],a[:],a[:]

def check(A):
    for i in range(1,N):
        now = 0 if s[i] == 'o' else 1
        temp = A[i-1] ^ A[i] ^ now
        if 1 <= i <= N-2:
            A[i+1] = temp
        else:
            if temp != A[0]:
                return
    now = 0 if s[0] == 'o' else 1
    if A[N-1] ^ A[0] ^ A[1] ^ now:
        return
    return A

A1[0],A1[1] = 0,0
A2[0],A2[1] = 0,1
A3[0],A3[1] = 1,0
A4[0],A4[1] = 1,1

ans = []
ans.extend([check(A1),check(A2),check(A3),check(A4)])
for x in ans:
    if x is not None:
        x = map(str,x)
        print(''.join(x).replace('0','S').replace('1','W'))
        exit()

print(-1)