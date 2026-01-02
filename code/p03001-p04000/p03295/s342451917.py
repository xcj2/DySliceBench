from functools import partial
from itertools import islice


def take(n, iterable):
    return list(islice(iterable, n))


def chunked(iterable, n):
    return iter(partial(take, n, iter(iterable)), [])


def solve(string):
    n, m, *ab = map(int, string.split())
    ab = sorted([tuple(_ab) for _ab in chunked(ab, 2)])
    cl = cr = None
    ans = 0
    for a, b in ab:
        if cr is None or cr <= a:
            cl, cr = a, b
            ans += 1
            continue
        cl, cr = max(cl, a), min(cr, b)
    return str(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m)])))
