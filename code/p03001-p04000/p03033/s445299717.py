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


from bisect import bisect_left

n, q = li()

stx = [list(li()) for _ in range(n)]
d = [ni() for _ in range(q)]

stx.sort(key=lambda x: x[2])

ans = [-1]*q
skip = [-1]*q

for si, ti, xi in stx:
    left = bisect_left(d, si-xi)
    right = bisect_left(d, ti-xi)

    while left < right:
        if skip[left] == -1:
            ans[left] = xi
            skip[left] = right
            left += 1

        else:
            left = skip[left]

print(*ans, sep="\n")