#!/usr/bin/env python3
import sys
# sys.setrecursionlimit(10000000)
INF = 1<<32


from bisect import bisect_left, bisect_right

def solve(N: int, M: int, A: "List[int]"):
        
    def binary_search(left: int, right: int):
        s = 0
        c = 0
        mi = INF

        while right-left > 1 or c < M:
            # print("test: ", left, " ", right)
            mid = (left+right)//2
            # print("mid: ", mid)
            # mid以上の価値の握手の個数を求める
            # s = []
            s = 0
            c = 0
            mi = INF
            for i in range(N):
                p = bisect_left(A, mid-A[i])
                if p != N:
                    mi = min(mi, A[i]+A[p])
                # print(A[i], A[p:], aq[N]-aq[p],  A[i]*(N-p))
                s += aq[N]-aq[p]
                s += A[i]*(N-p)
                c += N-p
                
            # mid以上の握手の個数がM以上か否か
            if c > M:
                left = mid

            else:
                right = mid
        
        if c > M:
            s -= (c-M)*mi

        return s

    A.sort()
    aq = [0] * (N+1)
    for i in range(N):
        aq[i+1] = aq[i] + A[i]

    print(binary_search(1, A[-1]*2))
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
