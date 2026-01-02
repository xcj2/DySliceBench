import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


class TestObj(object):

    def __init__(self, b, l, u, x):
        self.aokip = b
        self.minval = l
        self.maxval = u
        self.maxp = l * b + u * (x-b)

    def calc_point(self, r, x):
        return self.minval * min(self.aokip, r) + self.maxval * max(0, r - self.aokip)


def judge(tests, cum, n, k, x, thr):
    q = k // x
    r = k % x
    takap = 0

    if q >= n:
        return True

    for i in range(1,n+1):
        if i <= q:
            takap = max(takap, cum[q+1] - tests[i].maxp + tests[i].calc_point(r,x))

        else:
            takap = max(takap, cum[q] + tests[i].calc_point(r,x))

        if takap >= thr:
            return True

    return False


def binary_search(tests, x):
    n = len(tests) - 1

    thr = sum([ti.minval * ti.aokip for ti in tests])

    if thr == 0:
        return 0

    low = 0
    high = 10**18

    cum = []
    for ti in tests:
        if len(cum) > 0:
            cum.append(cum[-1] + ti.maxp)
        else:
            cum.append(0)

    while high - low > 1:
        mid = (high+low) // 2

        if judge(tests, cum, n, mid, x, thr):
            high = mid

        else:
            low = mid

    return high

n, x = li()
tests = []
for _ in range(n):
    b,l,u = li()
    tests.append(TestObj(b,l,u,x))

tests.sort(key=lambda x: x.maxp, reverse=True)
tests = [TestObj(0,0,0,x)] + tests
print(binary_search(tests, x))