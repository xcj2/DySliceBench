#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def solve(N: int, A: "List[int]"):
    if N == 0:
        if A[0] == 1:
            print(1)
        else:
            print(-1)
        return
        
    ans = 2 ** (N + 1) - 1
    len_list = []
    current_len = 1
    for depth, leafs in enumerate(A):
        ans -= leafs * (2 ** (N - depth + 1) - 2)
        len_list.append(current_len - leafs)
        current_len = (current_len - leafs) * 2
    last_leaf = len_list[-1]
    if last_leaf < 0:
        print(-1)
        return
    must_delete = last_leaf
    # print(must_delete)
    for _depth, x in enumerate(len_list[::-1]):
        depth = N - _depth
        leaf = A[depth]
        if must_delete <= (x + leaf) // 2:
            ans -= must_delete
            if ans > 0:
                print(ans)
            else:
                print(-1)
            return
        ans -= must_delete
        must_delete -= (x + leaf) // 2
    print(-1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 0 + 1)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
