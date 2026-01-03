import sys
from collections import deque
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
    a = list(mi())
    d = deque()
    for i in range(n):
        if i%2:
            d.appendleft(a[i])
        else:
            d.append(a[i])
    print(*list(d)[::((-1)**(n%2))])


if __name__ == '__main__':
    main()
