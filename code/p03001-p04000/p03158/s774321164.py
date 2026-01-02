from bisect import bisect_left
import sys
if sys.version_info[0:2] >= (3, 3):
    from collections.abc import Sequence
else:
    from collections import Sequence


class LazySequence(Sequence):
    def __init__(self, f, n):
        self.f = f
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if not (0 <= i < self.n):
            raise IndexError
        return self.f(i)


N, Q = map(int, input().split())
A = [int(s) for s in input().split()]
X = []
for _ in range(Q):
    X.append(int(input()))

# A.sort()
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + A[i - 1]
t = [0, A[0]] + [0] * (N - 1)
for i in range(2, N + 1):
    t[i] = t[i - 2] + A[i - 1]


def index_left(x, i):
    val = 2 * x - A[i]
    return bisect_left(A, val)


def nankaime(x, i):
    """requires x <= A[i]"""
    return i - index_left(x, i) + 1


def npi(x, i):
    return nankaime(x, i) + i


def index_right(x, istart):
    ls = LazySequence(lambda i: npi(x, i + istart), N - istart)
    return istart + bisect_left(ls, N) - 1


def getans(x):
    istart = bisect_left(A, x)
    if istart == N:
        return t[N]
    j = index_right(x, istart)
    turn = N - 1 - j
    i = j - turn + 1
    return s[N] - s[j + 1] + (t[i] if i > 0 else 0)


for i in range(Q):
    print(getans(X[i]))
