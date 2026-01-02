#!/usr/bin/env python3
import sys


def solve(X: int, Y: int, Z: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    C.sort(reverse=True)
    ret = []
    idx = [0] * Z
    for i in range(K):
        tmp = -1
        cur = -1
        for j in range(Z):
            if idx[j] < len(AB) and C[j] + AB[idx[j]] > tmp:
                tmp = C[j] + AB[idx[j]]
                cur = j
        ret.append(tmp)
        idx[cur] += 1
    for r in ret:
        print(r)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(X) ]  # type: "List[int]"
    B = [ int(next(tokens)) for _ in range(Y) ]  # type: "List[int]"
    C = [ int(next(tokens)) for _ in range(Z) ]  # type: "List[int]"
    solve(X, Y, Z, K, A, B, C)

if __name__ == '__main__':
    main()
