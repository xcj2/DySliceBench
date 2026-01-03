from itertools import groupby
from functools import reduce

MOD = 1000000007

def mod_pow(x, k):
    ret = 1
    while k > 0:
        if k & 1:
            ret *= x
            ret %= MOD
        k >>= 1
        x *= x
        x %= MOD
    return ret


def max_t():
    i, t_max = 0, 0
    for j, v in enumerate(t):
        if v < t_max:
            print(0)
            quit(0)
        if v > t_max:
            t_max = v
            i = j
    return i, t_max


def validate_a(i, t_max):
    for v in a[:i + 1]:
        if v != t_max:
            print(0)
            quit(0)
    for v in a[i + 1:]:
        if v > t_max:
            print(0)
            quit(0)


if __name__ == '__main__':
    n = int(input())
    t = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    i, t_max = max_t()
    validate_a(i, t_max)

    highests = [min(x, y) for x, y in zip(a, t)]
    print(reduce(lambda x, y: x * y % MOD, (mod_pow(v, ((length - 1) if v < t_max else max(length - 2, 0))) for v, length in ((v, len(list(l))) for v, l in groupby(highests)))))
