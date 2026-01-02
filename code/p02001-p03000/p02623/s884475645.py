import sys
from itertools import accumulate
import bisect

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, M, K = mi()
    A = list(mi())
    B = list(mi())

    Aacc = [0]+list(accumulate(A))
    Bacc = list(accumulate(B))
    Baccz = [0]+Bacc

    m = 0

    # print(Aacc)
    # print(Bacc)

    for i in range(N+1):
        t = Aacc[i]
        j = bisect.bisect_right(Bacc, K-t)
        if Aacc[i]+Baccz[j] <= K:
            m = max(m, i+j)

    print(m)


if __name__ == '__main__':
    main()
