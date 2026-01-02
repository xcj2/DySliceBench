import re
from itertools import count
from sys import stdin


def main():
    _, t, a, *hs = get_params()
    print(solve(t, a, hs))


def get_params():
    return map(int, words(get_contents()))


def words(s):
    return re.split(r'\s', s)


def get_contents():
    return stdin.read().strip()


def solve(t, a, hs):
    def temperature(h):
        return t - 0.006 * h

    def distance(t):
        return abs(t - a)

    ts = map(temperature, hs)
    ds = map(distance, ts)
    dis = zip(ds, count(1))
    return min(dis)[1]


if __name__ == '__main__':
    main()
