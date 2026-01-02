from functools import partial
from itertools import islice


def take(n, iterable):
    return list(islice(iterable, n))


def chunked(iterable, n):
    return iter(partial(take, n, iter(iterable)), [])


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def solve(s):
    h, w, d, *aqlr = map(int, s.split())
    a, q, lr = aqlr[:h * w], aqlr[h * w], aqlr[h * w + 1:]
    n = h * w
    pos = [0] * (n + 1)
    for i, _a in enumerate(a):
        pos[_a] = (i // w, i % w)
    cost = [0] * (n + 1)
    for i in range(d + 1, n + 1):
        cost[i] = cost[i - d] + distance(pos[i - d], pos[i])
    return "\n".join(["%d" % (cost[r] - cost[l]) for l, r in chunked(lr, 2)])


n, m, d = map(int, input().split())
l = '{} {} {}\n'.format(n, m, d) + '\n'.join([input() for _ in range(n)])
q, = map(int, input().split())
l += '\n{}\n'.format(q) + '\n'.join([input() for _ in range(q)])
print(solve(l))
