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
    H, W = read_values()
    C = tuple(read_index())
    D = tuple(read_index())
    S = [input().strip() for _ in range(H)]

    F = [False] * (H * W)

    M = {C}
    Q = [C]
    F[C[0] * W + C[1]] = 0
    c = 0
    while len(M) > 0:
        M.clear()
        while Q:
            h, w = Q.pop()
            M.add((h, w))
            if (h, w) == D:
                print(c)
                return

            for d in (1, -1):
                if 0 <= w + d < W and S[h][w + d] == "." and not F[h * W + w + d]:
                    F[h * W + w + d] = True
                    Q.append((h, w + d))
                if 0 <= h + d < H and S[h + d][w] == "." and not F[(h + d) * W + w]:
                    F[(h + d) * W + w] = True
                    Q.append((h + d, w))
        for h, w in M:
            for hh in range(h - 2, h + 3):
                for ww in range(w - 2, w + 3):
                    if 0 <= ww < W and 0 <= hh < H and S[hh][ww] == "." and not F[hh * W + ww]:
                        F[hh * W + ww] = True
                        Q.append((hh, ww))
        c += 1
    print(-1)
            

if __name__ == "__main__":
    main()

