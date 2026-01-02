import sys
from itertools import product

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def solve753(K):
    tmp = []
    for v in product('357', repeat=K):
        if len(set(v)) == 3:
            tmp.append(int(''.join(v)))
    return tmp


def main():
    N = ii()
    d = len(str(N))
    cnt = 0
    for i in range(1, d+1):
        for v in solve753(i):
            if v <= N:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
