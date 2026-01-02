import sys
from collections import deque


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    h, w = nm()
    Ch, Cw = nm()
    Dh, Dw = nm()
    S = [list(ns()) for _ in range(h)]
    pos = deque([(Ch, Cw)])
    cost = [[float('Inf')] * w for _ in range(h)]
    cost[Ch - 1][Cw - 1] = 0


    warp = deque([(Ch, Cw)])
    while pos:
        while pos:
            c_i, c_j = pos.pop()
            for i, j in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                if 0 <= c_i + i - 1 < h and 0 <= c_j + j - 1 < w \
                        and cost[c_i + i - 1][c_j + j - 1] > cost[c_i - 1][c_j - 1] \
                        and S[c_i + i - 1][c_j + j - 1] == '.':
                    cost[c_i + i - 1][c_j + j - 1] = cost[c_i - 1][c_j - 1]
                    pos.append((c_i + i, c_j + j))
                    warp.append((c_i + i, c_j + j))

        warp_sub = []
        while warp:
            c_i, c_j = warp.pop()
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if 0 <= c_i + i - 1 < h and 0 <= c_j + j - 1 < w \
                            and cost[c_i + i - 1][c_j + j - 1] > cost[c_i - 1][c_j - 1] + 1 \
                            and S[c_i + i - 1][c_j + j - 1] == '.':
                        cost[c_i + i - 1][c_j + j -
                                          1] = cost[c_i - 1][c_j - 1] + 1
                        pos.append((c_i + i, c_j + j))
                        warp_sub.append((c_i + i, c_j + j))

        warp.extend(warp_sub)

    print(cost[Dh - 1][Dw - 1] if cost[Dh - 1][Dw - 1] != float('Inf') else -1)


if __name__ == '__main__':
    main()
