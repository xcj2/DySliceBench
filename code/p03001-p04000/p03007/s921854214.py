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
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()
A = III()
A.sort(reverse=True)
plus = 0
for a in A:
    if a>0:
        plus += 1
if plus==N:
    plus -= 1

ans = []
val = A[plus]

if plus:
    for i in range(1,plus)[::-1]:
        ans.append((val,A[i]))
        val -= A[i]
    ans.append((A[0],val))
    val = A[0]-val

for i in range(plus+1,N):
    ans.append((val,A[i]))
    val -= A[i]

print(val)
for a in ans:
    print(*a, sep=' ')