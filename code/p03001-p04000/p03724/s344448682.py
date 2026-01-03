#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    edge_weights = [0]*(N+1)
    # edge_weights[i] = iとi+1を繋ぐへんの重み
    for i in range(M):
        edge_weights[a[i]] += 1
        edge_weights[b[i]] -= 1
    
    from itertools import accumulate

    edge_weights = list(accumulate(edge_weights))
    for i in range(N+1):
        if edge_weights[i]%2 == 0:
            continue
        else:
            print(NO)
            return
    
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
