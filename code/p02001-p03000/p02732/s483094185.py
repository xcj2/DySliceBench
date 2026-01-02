import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter
from bisect import bisect_left

def f(i, d, dsum, n):
    return func(i, d) + dsum[i] + dsum[n] - dsum[i+1]

def func(i, w):
    return w[i][1] * max(0, w[i][1]-1) // 2

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    d = dict(Counter(v))
    w = []
    for k in sorted(d.keys()):
        w.append([k, d[k]])
    m = len(w)
    c = [0] * (m+1)
    for i in range(1, m+1):
        c[i] = c[i-1] + func(i-1, w)
        # print(func(i-1, w))
    q = [u[0] for u in w]
    # print(c)
    # print(w)
    for i in v:
        g = bisect_left(q, i)
        # print(q)
        # print(i)
        # print('g: ', g)
        w[g][1] -= 1
        print(f(g, w, c, m))
        w[g][1] += 1


if __name__ == '__main__':
    main()
