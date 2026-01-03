#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: int, B: int, h: "List[int]"):
    def can(n, A, B, a):
        tmp = 0
        base = B * n
        diff = A - B
        for v in a:
            rest = v - base
            if rest > 0:
                tmp += (rest - 1) // diff + 1
        if tmp <= n:
            return True
        return False
    h.sort(reverse=True)
    mx = h[0]
    l = 0
    r = (mx - 1) // B + 1
    while r - l > 1:
        m = (r + l) // 2
        if can(m, A, B, h):
            r = m
        else:
            l = m
    #print(l, r)
    ret = r
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B, h)

if __name__ == '__main__':
    main()
