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

from collections import deque
from bisect import bisect_right
S = deque(list(str(input())))
Q = I()

one = []
isone = []
F = [0]*Q
C = [0]*Q
for i in range(Q):
    q = input().split()
    if q[0]=='1':
        one.append(i)
        isone.append(True)
    else:
        F[i] = (int(q[1]))
        C[i] = q[2]
        isone.append(False)


num = sum(isone)
if num%2==1:
    S = deque(list(reversed(S)))

bef = deque([])
aft = deque([])
for i,now in enumerate(isone):
    if now==1:
        if num%2==1:
            for b in reversed(bef):
                S.append(b)
            for a in aft:
                S.appendleft(a)
        else:
            for b in reversed(bef):
                S.appendleft(b)
            for a in aft:
                S.append(a)
        bef = deque([])
        aft = deque([])
        num -= 1
    else:
        if F[i]==1:
            bef.appendleft(C[i])
        else:
            aft.append(C[i])
for b in reversed(bef):
    S.appendleft(b)
for a in aft:
    S.append(a)
print(*S,sep='')