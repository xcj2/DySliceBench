#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(s, Q, queries):
    l = ['']
    r = ['']
    rev = 0
    for q in queries:
        if q[0] == 1:
            rev += 1
            continue
        f = q[1]
        c = q[2]
        if rev % 2 == 0 and f == 2 or rev % 2 == 1 and f == 1:
            r.append(c)
        else:
            l.append(c)
    if rev % 2 == 0:
        l.reverse()
        ret = ''.join(l) + s + ''.join(r)
    else:
        r.reverse()
        ret = ''.join(r) + s[::-1] + ''.join(l)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = str(next(tokens))
    Q = int(next(tokens))
    q = []
    for i in range(Q):
        t = int(next(tokens))
        if t == 1:
            q.append([1, None, None])
        else:
            f = int(next(tokens))
            c = str(next(tokens))
            q.append([2, f, c])
    solve(s, Q, q)

if __name__ == '__main__':
    main()
