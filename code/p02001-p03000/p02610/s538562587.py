import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from heapq import heappop, heappush
def solve():
    N = int(input())
    Ls = [[] for _ in range(N)]
    Rs = [[] for _ in range(N)]
    base = 0
    for _ in range(N):
        k, l, r = mapint()
        if l>=r:
            Ls[k-1].append(l-r)
            base += r
        else:
            if N-k!=0:
                Rs[N-k-1].append(r-l)
            base += l
    return base + calculate(Ls, N) + calculate(Rs, N)


def calculate(lis, N):
    queue = []
    for i in range(N):
        for x in lis[i]:
            heappush(queue, x)
        while len(queue)>i+1:
            heappop(queue)
    return sum(queue)


T = int(input())
for t in range(T):
    print(solve())