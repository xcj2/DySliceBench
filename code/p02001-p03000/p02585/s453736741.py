import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
from collections import Counter
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def accumurate(l):
    ret = [0] * len(l)
    ret[0] = l[0]

    for i in range(1, len(l)):
        ret[i] = ret[i - 1] + l[i]

    return ret


def main():
    n, k = geta(int)
    p = [0] + list(geta(int))
    c = [0] + list(geta(int))

    inf = 1 << 32

    used = [False] * (n + 1)

    ans = -inf

    for i in range(1, n + 1):

        if used[i]:
            continue
        else:
            used[i] = True

        c_loop = []
        j = p[i]
        c_loop += [c[j]]

        while j != i:
            used[j] = True
            j = p[j]
            c_loop += [c[j]]

        n_loop = len(c_loop)
        c_loop += c_loop
        cs_loop = accumurate(c_loop)
        tot_loop = cs_loop[n_loop - 1]

        _jmax = k if k < n_loop else n_loop

        _ans = -inf
        _len = 0
        for _i in range(n_loop):
            for _j in range(1, _jmax + 1):
                _tmp = cs_loop[_j + _i] - cs_loop[_i]

                if tot_loop > 0 and k > _j:
                    _tmp += (k - _j) // n_loop * tot_loop

                if _ans < _tmp:
                    _ans = _tmp

        if ans < _ans:
            ans = _ans

    print(ans)


if __name__ == "__main__":
    main()