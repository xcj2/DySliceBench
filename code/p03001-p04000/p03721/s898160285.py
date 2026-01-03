import sys
from collections import defaultdict
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
    N, K = mi()
    a, b = i2(N)
    d = defaultdict(int)
    for i in range(N):
        d[a[i]] += b[i]
    d = [(k, v) for k, v in d.items()]
    d.sort()
    s = 0
    for k, v in d:
        s += v
        if s >= K:
            print(k)
            return



if __name__ == '__main__':
    main()
