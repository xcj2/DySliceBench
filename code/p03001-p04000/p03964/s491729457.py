#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, T: "List[int]", A: "List[int]"):
    t, a = 1, 1
    for i in range(N):
        if T[i] == A[i]:
            tmp = max(t, a)
            t = tmp
            a = tmp
        elif t <= a / A[i] * T[i]:
            a = ((a - 1) // A[i] + 1) * A[i]
            t = (a // A[i]) * T[i]
        else:
            t = ((t - 1) // T[i] + 1) * T[i]
            a = (t // T[i]) * A[i]
        #print(T[i], A[i], t, a)
    ret = a + t
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]" 
    A = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        T[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, T, A)

if __name__ == '__main__':
    main()
