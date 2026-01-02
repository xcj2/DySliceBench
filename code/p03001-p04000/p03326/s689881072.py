from functools import partial
from itertools import islice, product


def take(n, iterable):
    return list(islice(iterable, n))


def chunked(iterable, n):
    return iter(partial(take, n, iter(iterable)), [])


def solve(s):
    n, m, *xyz = map(int, s.split())
    return max([
        sum(
            sorted([x * sign_x + y * sign_y + z * sign_z for x, y, z in chunked(xyz, 3)],
                   reverse=True)[:m]) for sign_x, sign_y, sign_z in product([1, -1], repeat=3)
    ])


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
