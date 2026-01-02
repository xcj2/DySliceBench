# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign

def main():
    N, K = mi()
    A = lmi()
    F = lmi()
    A.sort()
    F.sort()
    F.reverse()
    ng = -1
    ok = 10**12
    while ok - ng > 1:
        mid = (ok + ng) // 2
        t = 0
        for i in range(N):
            t += max(A[i] - mid // F[i], 0)
        if t <= K:
            ok = mid
        else:
            ng = mid
    print(ok)
    return


if __name__ == '__main__':
    main()
