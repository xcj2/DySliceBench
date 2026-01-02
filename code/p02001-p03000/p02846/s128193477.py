#!/usr/bin/env python3

def binsearch(l, r, pred):  # [l, r)
    assert l < r
    l -= 1
    while r - l > 1:
        m = (l + r) // 2
        if pred(m):
            r = m
        else:
            l = m
    return r

def solve(t1, t2, a1, a2, b1, b2):
    assert a1 != b1
    assert a2 != b2
    if a1 > b1:
        a1, b1 = b1, a1
        a2, b2 = b2, a2
    assert a1 < b1
    if a1 * t1 + a2 * t2 < b1 * t1 + b2 * t2:
        return 0
    elif a1 * t1 + a2 * t2 == b1 * t1 + b2 * t2:
        return 'infinity'
    else:

        def f(k):
            x0 = (a1 * t1 + a2 * t2) * k
            y0 = (b1 * t1 + b2 * t2) * k
            x1 = x0 + a1 * t1
            y1 = y0 + b1 * t1
            x2 = x1 + a2 * t2
            y2 = y1 + b2 * t2
            if y0 <= x0 and x1 < y1 and y2 < x2:
                return 2
            elif y0 <= x0 and x1 < y1 and y2 <= x2:
                return 1
            elif y0 <= x0 and x1 == y1:
                return 1
            else:
                return 0
        def pred(k):
            return f(k) == 0
        k = binsearch(0, 10 ** 18, pred)
        return 2 * (k - 1) + f(k - 1) - 1

def main():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    print(solve(t1, t2, a1, a2, b1, b2))

if __name__ == '__main__':
    main()
