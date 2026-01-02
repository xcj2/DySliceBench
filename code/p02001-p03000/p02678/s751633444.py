import sys
from collections import deque
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, M = na()
node_dic = {}
for _ in range(M):
    A, B = na()
    if B in node_dic:
        node_dic[B].append(A)
    else:
        node_dic[B] = [A]
    if A in node_dic:
        node_dic[A].append(B)
    else:
        node_dic[A] = [B]


edge = deque()
edge.append(1)
d = [-1] * N
d[0] = 0
while len(edge):
    e = edge.popleft()
    for ee in node_dic[e]:
        if d[ee - 1] == -1:
            d[ee - 1] = e
            edge.append(ee)
if -1 in d:
    print("No")
else:
    print("Yes")
    print("\n".join(map(str, d[1:])))
