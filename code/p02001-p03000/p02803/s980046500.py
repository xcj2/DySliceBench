from collections import deque, defaultdict
from itertools import chain, combinations
import json


def main():
    # N = int(input())
    H, W = [int(a) for a in input().split()]
    S = [
        input()
        for _ in range(H)
    ]

    def saitan(start, end):
        mem = {start}

        def get_rinsetsu(ii, jj):
            d = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ]
            res = []
            for di, dj in d:
                ni = ii + di
                nj = jj + dj
                if ni < 0 or nj < 0:
                    continue
                if ni >= H or nj >= W:
                    continue
                if S[ni][nj] == '.':
                    if (ni, nj) not in mem:
                        res.append((ni, nj))
            return res

        q = [(start, 0)]
        while len(q) != 0:
            (i, j), distance = q.pop(0)
            rinsetsu = get_rinsetsu(i, j)
            for r in rinsetsu:
                if r == end:
                    return distance + 1, mem
                q.append((r, distance + 1))
                mem.add(r)
        return -1, mem

    res = -1
    for a in range(H * W):
        start = a // W, a % W
        mm = set()
        if S[start[0]][start[1]] == '#':
            continue
        for b in range(a + 1, H * W):
            end = b // W, b % W
            if S[end[0]][end[1]] == '#':
                continue
            if end in mm:
                continue
            ddd, m = saitan(start, end)
            mm |= m
            res = max(res, ddd)
    print(res)


if __name__ == "__main__":
    main()
