from collections import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    k = int(input())
    dist = [-1] * k
    q = deque()
    q.append([1, 1])
    while q:
        d, u = q.popleft()
        if dist[u] != -1: continue
        dist[u] = d
        if u == 0:
            print(d)
            break
        v = (u + 1) % k
        if dist[v] == -1: q.append([d + 1, v])
        v = (u * 10) % k
        if dist[v] == -1: q.appendleft([d, v])

main()
