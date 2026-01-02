#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[int]", y: "List[int]", h: "List[int]"):
    def is_match_to_samples(cx, cy):
        hmax = max(h)
        hmax_idx = h.index(hmax)
        ht = top_height(cx, cy, x[hmax_idx], y[hmax_idx], hmax)
        for xi, yi, hi in zip(x, y, h):
            if hi != height(cx, cy, xi, yi, ht):
                return False, -1
        return True, ht

    import itertools
    for cx, cy in itertools.product(range(101), range(101)):
        is_match, ht = is_match_to_samples(cx, cy)
        if is_match:
            print("{} {} {}".format(cx, cy, ht))
            break
    return

def height(cx, cy, xi, yi, ht):
    return max(0, ht - abs(cx - xi) - abs(cy - yi))

def top_height(cx, cy, xi, yi, hi):
    return hi + abs(cx - xi) + abs(cy - yi)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]" 
    y = [int()] * (N)  # type: "List[int]" 
    h = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, x, y, h)

if __name__ == '__main__':
    main()
