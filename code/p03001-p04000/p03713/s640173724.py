#!/usr/bin/env python3
import sys
INF = float("inf")


def argmin(a):
    m, n = 1 << 31, -1
    for i, v in enumerate(a):
        if m > v:
            m, n = v, i
    return m, n


def ternary_search(f, x0, x3):
    """
    3分探索を行う。下に凸な関数fの、区間[x0, x3]内にある極値を探し、(x, f(x))を返す。
    なければ、区間の端点が返る。
    fは整数引数、x0,x3も整数引数とする。
    """
    if x0 + 2 == x3:
        xs = [x0, x0+1, x0+2]
        v, i = argmin(list(map(f, xs)))
        return xs[i], v

    x1 = (2*x0+x3)//3
    x2 = (x0+2*x3)//3

    if f(x1) >= f(x2):
        return ternary_search(f, x1, x3)
    else:
        return ternary_search(f, x0, x2)


def solve(H: int, W: int):
    if H % 3 == 0 or W % 3 == 0:
        print(0)
        return

    cand = INF
    y = 1

    def g(x, y):
        return max(x*y, W*(H-y), y*(W-x))-min(x*y, W*(H-y), y*(W-x))

    def h(x, y):
        return max(x*y, x*(H-y), H*(W-x))-min(x*y, x*(H-y), H*(W-x))

    if H == W == 2:
        print(1)
        return
    else:
        cand = min(cand, min(H, W))

    y0, y3 = 1, H-1
    x = W//2
    while y0 + 2 < y3:
        y1 = (2*y0+y3)//3
        y2 = (y0+2*y3)//3
        S1 = g(x, y1)
        S2 = g(x, y2)
        if S1 >= S2:
            y0 = y1
        else:
            y3 = y2
    ys = [y0, y0+1, y0+2]
    for y in ys:
        S = g(x, y)
        cand = min(S, cand)

    x0, x3 = 1, W-1
    y = H//2
    while x0 + 2 < x3:
        x1 = (2*x0+x3)//3
        x2 = (x0+2*x3)//3
        S1 = h(x1, y)
        S2 = h(x2, y)
        if S1 >= S2:
            x0 = x1
        else:
            x3 = x2
    xs = [x0, x0+1, x0+2]
    for x in xs:
        S = h(x, y)
        cand = min(S, cand)
    print(cand)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(H, W)


if __name__ == '__main__':
    main()
