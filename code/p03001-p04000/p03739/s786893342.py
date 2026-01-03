#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

def solve(n: int, a: "List[int]"):
    tmp = 0
    s = 0
    for i, v in enumerate(a):
        s += v
        if i % 2 == 0 and s <= 0:
            tmp += abs(s) + 1
            s = 1
        elif i % 2 != 0 and s >= 0:
            tmp += abs(s) + 1
            s = -1
    ret = tmp
    tmp = 0
    s = 0
    for i, v in enumerate(a):
        s += v
        if i % 2 == 0 and s >= 0:
            tmp += abs(s) + 1
            s = -1
        elif i % 2 != 0 and s <= 0:
            tmp += abs(s) + 1
            s = 1
    ret = min(ret, tmp)
    print(ret)

def _solve(n: int, a: "List[int]"):
    o, e = 0, 0
    tmp = 0
    for i, v in enumerate(a):
        if i % 2 == 0:
            e += v
            if e < 0:
                tmp += abs(e) + 1
                e = 1
            else:
                tmp += max(0, abs(o) - abs(e) + 1)
                e += tmp
        else:
            o += v
            if o > 0:
                tmp += abs(o) + 1
                o = -1
            else:
                tmp += max(0, abs(e) - abs(o) + 1)
                o -= tmp
    ret = tmp

    o, e = 0, 0
    tmp = 0
    for i, v in enumerate(a):
        if i % 2 == 0:
            e += v
            if e > 0:
                tmp += abs(e) + 1
                e = -1
            else:
                tmp += max(0, abs(o) - abs(e) + 1)
                e -= tmp
        else:
            o += v
            if o < 0:
                tmp += abs(o) + 1
                o = 1
            else:
                tmp += max(0, abs(e) - abs(o) + 1)
                o += tmp
    ret = min(ret, tmp)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
