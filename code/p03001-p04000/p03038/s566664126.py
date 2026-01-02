#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    A.sort()                    # 昇順 O(NlongN)
    BC = list(zip(B, C))
    BC.sort(key=lambda x: x[1])  # 昇順 MlogM

    s = 0
    Cs = []
    for i, a in enumerate(A):
        if len(Cs) == 0:
            if len(BC) == 0:
                s += sum(A[i:])
                break
            b, c = BC.pop(-1)
            Cs.extend([c]*b)
        s += max(Cs.pop(), a)
    print(s)
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
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)


if __name__ == '__main__':
    main()
