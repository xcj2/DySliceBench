import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter, defaultdict
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import queue
import bisect
MOD = 10**9 + 7
from logging import getLogger, StreamHandler, DEBUG, WARNING
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
# handler.setLevel(WARNING)
# logger.setLevel(WARNING)
logger.addHandler(handler)
def main():
    INF = 10 ** 7
    n, m = getList()
    kempa = [[] for i in range(3 * n)]
    costs = [INF for i in range(3 * n)]
    for _ in range(m):
        u, v = getList()
        kempa[3 * u - 3].append(3 * v - 2)
        kempa[3 * u - 2].append(3 * v - 1)
        kempa[3 * u - 1].append(3 * v - 3)

    # =================--探索===================
    s, t = getList()
    deq = deque()
    deq.append(3 * s - 3)
    costs[3 * s - 3] = 0
    while(deq):
        tmp = deq.popleft()
        tcost = costs[tmp]
        for nxt in kempa[tmp]:
            if costs[nxt] > tcost + 1:
                deq.append(nxt)
                costs[nxt] = tcost + 1
    # =================--探索===================
    # print(costs)
    if costs[t * 3 - 3] == INF:
        print(-1)
    else:
        print(costs[t * 3 - 3] // 3)

if __name__ == "__main__":
    main()