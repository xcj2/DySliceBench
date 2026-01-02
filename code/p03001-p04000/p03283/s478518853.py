import sys
sys.setrecursionlimit(500000)

def memoize(f):
    table = {}

    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func


@memoize
def memo(a, b):
    if a == b:
        return e[a].count(a)
    elif b - a == 1:
        return memo(b, b) + memo(a, a) + e[a].count(b)
    else:
        return memo(a+1, b)+memo(a, b-1) + e[a].count(b) - memo(a+1, b-1)


n, m, q = map(int, input().split())
e = []
for i in range(n+1):
    e.append([])
for i in range(m):
    x, y = map(int, input().split())
    e[x].append(y)
for i in range(q):
    x, y = map(int, input().split())
    print(memo(x, y))
