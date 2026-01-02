import sys


def memoize(f):
    memo = {}

    def main(*args):
        if args in memo:
            return memo[args]
        result = memo[args] = f(*args)
        return result

    return main


def get_num(remains):
    i = 0
    while remains:
        if remains & 1:
            yield i
        i += 1
        remains >>= 1


@memoize
def calc(n, s, remains):
    if n == 1:
        if remains & (1 << s):
            return 1
        else:
            return 0
    if s <= 0:
        return 0

    return sum(calc(n - 1, s - n * m, remains ^ (1 << m)) for m in get_num(remains) if s - n * m >= 0)


for line in sys.stdin:
    n, s = map(int, line.split())
    print(calc(n, s, (1 << 10) - 1))