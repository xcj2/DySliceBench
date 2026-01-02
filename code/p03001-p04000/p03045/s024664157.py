import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
 
def find(a, L):
    if L[a] == a: return a
    else: 
        L[a] = find(L[a], L)
        return L[a]
 
def unite(a, b, L, R):
    a = find(a, L)
    b = find(b, L)
    if a == b: return
    if R[a] < R[b]:
        L[a] = b
    else:
        L[b] = a
        if R[a] == R[b]: R[a] += 1
    
  
def solve():
    N, M = map(int, line_input())
    parent = [int(i) for i in range(N)]
    edge = [[] for i in range(N)]
    rank = [0] * N
    for i in range(M):
        x, y, z = map(int, line_input())
        unite(x-1, y-1, parent, rank)
    for i in range(N):
        parent[i] = find(i, parent)
    print(len(set(parent)))
    return 0
  
if __name__ == "__main__":
    solve()