import sys, math
from collections import defaultdict
from itertools import product
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    n = ii()
    S = [input() for i in range(n)]
    d = defaultdict(int)
    for c in S[0]:
        d[c] += 1
    for i in range(n):
        tmp = defaultdict(int)
        for c in S[i]:
            tmp[c] += 1
        for k in d.keys():
            d[k] = min(d[k], tmp[k])
    l = [k*v for k, v in d.items()]
    l = ''.join(sorted(''.join(l)))
    print(l)

if __name__ == '__main__':
    main()