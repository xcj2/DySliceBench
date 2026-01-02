import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

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
A = LI()
B = LI()

if N == 1:
    if A[0] == B[0]:
        print('No')
    else:
        print('Yes')
        print(B[0])
    exit()

def place(i,j):
    if 0 <= j-i<= N-1:
        return j-i
    else:
        return N+j-i


C = set()
for i in range(N):
    C.add(i)

de = defaultdict(list)
for i in range(N):
    de[B[i]].append(i)

a = 0
b = 0
cu = [0]*(N+1)
for i in range(1,N):
    if A[i-1] == A[i]:
        b += 1
    else:
        b = i-1
        if len(de[A[a]]) == 0:
            a = i
            continue
        else:
            c = de[A[a]][0]
            d = de[A[a]][-1]
            if d-a >= 0:
                left = max(0,min(c-a,d-b))
                right = d-a
                cu[left] += 1
                cu[right+1] -= 1
            if c < b:
                left = N+c-b
                right = min(N-1,max(N+d-b,N+c-a))
                cu[left] += 1
                cu[right+1] -= 1
            a = i

if len(de[A[a]]) == 0:
    a = i
else:
    c = de[A[a]][0]
    d = de[A[a]][-1]
    if d-a >= 0:
        left = max(0,min(c-a,d-b))
        right = d-a
        cu[left] += 1
        cu[right+1] -= 1
    if c < b:
        left = N+c-b
        right = min(N-1,max(N+d-b,N+c-a))
        cu[left] += 1
        cu[right+1] -= 1
    a = i


cumu = [0]*N
for i in range(N):
    cumu[i] = cumu[i-1]+cu[i]
#print(cumu)
for k in range(N):
    if cumu[k] <= 0:
        print('Yes')
        ans1 = [B[i+k] for i in range(N-k)]
        ans2 = [B[i-(N-k)] for i in range(N-k,N)]
        ans1.extend(ans2)
        print(*ans1)
        exit()

print('No')