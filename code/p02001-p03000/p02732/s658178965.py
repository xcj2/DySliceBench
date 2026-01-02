import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter
from bisect import bisect_left

def calc(d, i, dsum, m):
    return comb(d, i) + dsum[i] + dsum[m] - dsum[i+1]

def comb(d, i):
    return d[i][1] * max(0, d[i][1] - 1) // 2

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    d = [[k, v] for k, v in sorted(dict(Counter(v)).items())]
    keys = [q[0] for q in d]
    m = len(d)
    dsum = [0] * (n+1)
    for i in range(1, m+1):
        dsum[i] = dsum[i-1] + comb(d, i-1)
    for i in range(n):
        j = bisect_left(keys, v[i])
        d[j][1] -= 1
        print(calc(d, j, dsum, m))
        d[j][1] += 1

if __name__ == '__main__':
    main()
