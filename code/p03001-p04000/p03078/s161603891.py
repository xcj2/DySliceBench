#!/usr/bin/env python3
import sys


def solve(X: int, Y: int, Z: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    AB = []

    for i in range(X):
        for j in range(Y):
            AB.append(A[i]+B[j])
    AB.sort(reverse=True)
    AB = AB[:K]

    ABC = []
    for k in range(Z):
        for ab_index in range(len(AB)):
            ABC.append(C[k]+AB[ab_index])

    ABC.sort(reverse=True)
    ABC = ABC[:K]
    for i in range(len(ABC)):
        print(ABC[i])
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
    A = [int(next(tokens)) for _ in range(X)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(Y)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(Z)]  # type: "List[int]"
    solve(X, Y, Z, K, A, B, C)

if __name__ == '__main__':
    main()
