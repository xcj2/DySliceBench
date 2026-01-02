from functools import partial
from itertools import islice, accumulate


def take(n, iterable):
    return list(islice(iterable, n))


def chunked(iterable, n):
    return iter(partial(take, n, iter(iterable)), [])


def solve(s):
    n, m, q, *lrpq = map(int, s.split())
    lr, pq = lrpq[:2 * m], lrpq[2 * m:]
    t = [[0] * (n + 1) for _ in range(n + 1)]
    for l, r in chunked(lr, 2):
        t[l][r] += 1
    t = [list(accumulate(_t)) for _t in zip(*(accumulate(_t) for _t in t))]
    return "\n".join(
        [str(t[q][q] - t[q][p - 1] - t[p - 1][q] + t[p - 1][p - 1]) for p, q in chunked(pq, 2)])


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    print(solve('{} {} {}\n'.format(n, m, q) + '\n'.join([input() for _ in range(m + q)])))
