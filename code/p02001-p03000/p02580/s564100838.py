import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    H, W, M = read_values()
    T = [tuple(read_index()) for _ in range(M)]   

    HT = [0] * H
    WT = [0] * W
    for h, w in T:
        HT[h] += 1
        WT[w] += 1

    hm = max(HT)
    wm = max(WT)
    hs = set(h for h, v in enumerate(HT) if v == hm)
    ws = set(w for w, v in enumerate(WT) if v == wm)
    if len(hs) * len(ws) > M:
        print(hm + wm)
        return
    m = 0
    for h, w in T:    
        if h in hs and w in ws:
            m += 1

    print(hm + wm - (1 if len(hs) * len(ws) == m else 0))


if __name__ == "__main__":
    main()

