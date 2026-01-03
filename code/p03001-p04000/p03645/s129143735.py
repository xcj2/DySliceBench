#!/usr/bin/env python3
import sys

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str

def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    conn = [[] for _ in range(N)]
    for i in range(M):
        conn[a[i] - 1].append(b[i] - 1)
        conn[b[i] - 1].append(a[i] - 1)
    ret = NO
    for n in conn[0]:
        if N - 1 in conn[n]:
            ret = YES
    print(ret)
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
