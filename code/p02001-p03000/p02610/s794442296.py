import sys
import heapq
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


T = ni()

for _ in range(T):
    N = ni()
    ans = 0
    plus = []
    minus = []
    for _ in range(N):
        k, l, r = na()
        if l > r:
            plus.append([k, l-r])
            ans += r
        elif l < r:
            if N != k:
                minus.append([N-k, r-l])
            ans += l
        else:
            ans += l
    plus = sorted(plus, key=lambda x: x[0] * 10 ** 10 - x[1])
    minus = sorted(minus, key=lambda x: x[0] * 10 ** 10 - x[1])
    queue = []
    for p in plus:
        i, v = p 
        if len(queue) < i:
            heapq.heappush(queue, v)
        else:
            if queue[0] < v:
                heapq.heappushpop(queue, v)
    ans += sum(queue)
    queue = []
    for m in minus:
        i, v = m
        if len(queue) < i:
            heapq.heappush(queue, v)
        else:
            if queue[0] < v:
                heapq.heappushpop(queue, v)
    ans += sum(queue)
    print(ans)
