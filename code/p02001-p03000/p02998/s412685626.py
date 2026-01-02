# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap



@mt
def slv(N, XY):
    from collections import defaultdict
    g = defaultdict(set)
    yo = 10**6
    V = set()
    for x, y in XY:
        y += yo
        g[x].add(y)
        g[y].add(x)
        V.add(x)
        V.add(y)


    rem = set(v for v in V)
    done = set()
    ans = 0
    while rem:
        u = rem.pop()
        s = [u]
        done.add(u)
        xs = set()
        ys = set()
        if u >= yo:
            ys.add(u)
        else:
            xs.add(u)
        while s:
            u = s.pop()
            if u >= yo:
                ys.add(u)
            else:
                xs.add(u)
            for v in g[u]:
                if v in done:
                    continue
                s.append(v)
                done.add(v)
        rem -= xs
        rem -= ys
        e = 0
        for u in xs:
            e += len(g[u])
        ans += len(xs) * len(ys) - e

    return ans





def main():
    N = read_int()
    XY = [read_int_n() for _ in range(N)]
    print(slv(N, XY))


if __name__ == '__main__':
    main()
