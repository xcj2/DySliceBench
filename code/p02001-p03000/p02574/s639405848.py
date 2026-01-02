import sys
from functools import reduce
from operator import add


def _i(): return int(sys.stdin.readline().strip())


def _ia(): return map(int, sys.stdin.readline().strip().split())


def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


def main():
    n = _i()
    a = list(sorted(_ia()))
    r = a[0]
    for ai in a[1:]:
        r = gcd(r, ai)
        if r == 1:
            break
    else:
        return "not coprime"

    N = 10 ** 6 + 1
    f = [False] * N
    p = []
    k = {ai: 1 for ai in a}
    for i in range(2, N):
        if f[i]:
            continue
        p.append(i)

        tmp = 0
        if k.get(i) is not None:
            tmp += 1
        for j in range(2*i, N, i):
            f[j] = True
            if k.get(j) is not None:
                tmp += 1
                if tmp > 1:
                    return "setwise coprime"
    else:
        return "pairwise coprime"


if __name__ == "__main__":
    print(main())
