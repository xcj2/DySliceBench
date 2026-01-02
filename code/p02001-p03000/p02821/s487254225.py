#!/usr/bin/env python3
import sys
from itertools import accumulate
from bisect import bisect_left

def solve(N: int, M: int, A: "List[int]"):
    A.sort()

    right = 2*A[-1]+1
    left = 0

    while right - left > 1:
        mid = (left+right)//2

        # A[i]+A[j] >= midになるようなi,jの組み合わせの個数 mを 求めたい
        # m >= Mならok
        m = 0
        for i in range(N):
            a = A[i]
            res = mid - a
            # Aからres以上のものを探す
            index = bisect_left(A,res)
            m += N-index
        
        if m >= M:
            left = mid
        else:
            right = mid

    # M通り以上の握手ができる最小の組み合わせの幸福度
    B = sorted(A,reverse=True)
    accum_B = list(accumulate(B))
    answer = 0
    handshake_count = 0
    for i in range(N):
        res = left - A[i]
        if res > A[-1]:
            continue
        index = bisect_left(A,res)
        answer += (N-index)*A[i]+accum_B[N-index-1]
        handshake_count += (N-index)

    # 握手の回数がmを越えたときはその分の幸福度を引く
    if handshake_count>M:
        answer -= left*(handshake_count-M)
    print(answer)
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
