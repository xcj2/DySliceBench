import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools
from collections import deque
from heapq import heappop, heappush, heapify
from collections import defaultdict

N = int(readline())
A = list(map(lambda x: int(x) - 1,read().split())) + [-1]

def test(A,B):
    for x,y in zip(B, B[1:]):
        if A[x] == y:
            return False
    return True

def solve_small(cand, A, ng_first = -1):
    for p in itertools.permutations(cand):
        if p[0] == ng_first:
            continue
        if test(A, p):
            return p
    return False

if N <= 6:
    p = solve_small(range(N), A)
    if not p:
        print(-1)
        exit()
    print(' '.join(str(x+1) for x in p))
    exit()

in_deg = [0] * (N+10)
for x in A:
    in_deg[x] += 1

q = [(-x, i) for i,x in enumerate(in_deg)] # in_deg最大の人を分かるようにしたい
heapify(q)
se = set(q)

def greedy(rest,A,ng_first):
    B = []
    ng = ng_first
    while len(rest) >= 4:
        x = rest[0]; y = rest[1]
        if ng == x:
            B.append(y)
            rest.popleft()
            rest.popleft()
            rest.appendleft(x)
        else:
            B.append(x)
            rest.popleft()
        ng = A[B[-1]]
    return B

rest = deque(range(N))
B = []
prev = N
n = N
for _ in range(N-4):
    while q[0] not in se:
        heappop(q)
    if -q[0][0] == n - 1:
        v = q[0][1]
        B.append(v)
        rest.remove(v)
        B += greedy(rest, A, A[B[-1]])
        break
    x = rest[0]; y = rest[1]
    if A[prev] == x:
        B.append(y)
        rest.popleft()
        rest.popleft()
        rest.appendleft(x)
    else:
        B.append(x)
        rest.popleft()
    prev = B[-1]
    v = A[B[-1]]
    se.remove((-in_deg[v],v))
    in_deg[v] -= 1
    se.add((-in_deg[v],v))
    n -= 1
if len(B) < N:
    B += list(solve_small(rest, A, A[B[-1]]))

print(' '.join(str(x+1) for x in B))