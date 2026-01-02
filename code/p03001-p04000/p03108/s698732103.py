# coding: utf-8
import sys
stdin = sys.stdin

sr = lambda: stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
AB = [lr() for _ in range(M)]
V = [x for x in range(N+1)]
total = N * (N-1) // 2

def find(A, x):
    parent = A[x]
    if parent == x: return x
    root = find(A, parent)
    A[x] = root
    return root

def union(A, x, y):
    root, second = find(A, x), find(A, y)
    if root > second:
        second, root = root, second
    A[second] = root

def merge(A, x, y):
    root_A = find(A, a); root_B = find(A, b)
    if root_A == root_B:
        return 0
    ret = group[root_A] * group[root_B]
    new_group = group[root_A] + group[root_B]
    group[root_A] = group[root_B] = new_group
    union(A, a, b)
    return ret

conv = 0
answer = []
group = [1] * (N+1)
for a, b in AB[::-1]:
    answer.append(total - conv)
    conv += merge(V, a, b)

for x in answer[::-1]:
    print(x)
