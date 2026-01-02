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

def main():
    N = ii()
    A, B, C = [sorted(list(mi())) for i in range(3)]
    la = [bisect.bisect_left(A, b) for b in B]
    lc = [N-bisect.bisect_right(C, b) for b in B]
    print(sum(la[i]*lc[i] for i in range(N)))

if __name__ == '__main__':
    main()