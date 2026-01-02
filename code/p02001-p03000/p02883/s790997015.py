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

def judge(n, a, f, x, k):
    req = 0
    for i in range(n):
        if a[i]*f[i] > x:
            req += -(-(a[i]*f[i] - x) // f[i])
    return True if req <= k else False

def binsearch(n, a, f, k):
    low = 0
    high = max(a) * max(f)
    while high - low > 1:
        mid = (low + high) // 2
        if judge(n, a, f, mid, k):
            high = mid
        else:
            low = mid

    return high

n, k = li()
a = list(li())
f = list(li())

a.sort()
f.sort(reverse=True)

if k >= sum(a):
    print(0)
else:
    print(binsearch(n, a, f, k))