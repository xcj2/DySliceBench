import sys, math
import bisect
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

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i += 1
    return True

def main():
    l = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    K = ii()
    print(l[K-1])


if __name__ == '__main__':
    main()