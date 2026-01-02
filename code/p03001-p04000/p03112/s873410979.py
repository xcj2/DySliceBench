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

def find_left_right(lis: list, pos: int):
    left_idx = bisect_left(lis, pos) - 1
    left = lis[left_idx]
    right = lis[left_idx+1]
    return left, right

def find_min(sh_l, sh_r, tm_l, tm_r, x):
    ret = 10**18
    ret = min(ret, max(x-sh_l, x-tm_l))
    ret = min(ret, (tm_r - sh_l + min(x-sh_l, tm_r-x)))
    ret = min(ret, (sh_r - tm_l + min(x-tm_l, sh_r-x)))
    ret = min(ret, max(sh_r-x, tm_r-x))

    return ret

a,b,q = li()
INF = 10**18
s = [-INF] + [ni() for _ in range(a)] + [INF]
t = [-INF] + [ni() for _ in range(b)] + [INF]
x = [ni() for _ in range(q)]

for xi in x:
    shrine_left, shrine_right = find_left_right(s, xi)
    temple_left, temple_right = find_left_right(t, xi)
    print(find_min(shrine_left, shrine_right, temple_left, temple_right, xi))
