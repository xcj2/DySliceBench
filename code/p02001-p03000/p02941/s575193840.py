#!/usr/bin/env python3
import sys
# import heapq


def solve(N: int, A: "List[int]", B: "List[int]"):

    count = 0
    flag = True
    while flag:
        flag = False
        for i in range(N):
            a, b, c = B[i-1], B[i], B[(i+1) % N]
            if b > A[i] and b > a+c:
                d, m = divmod(b-A[i], a+c)
                if m == 0:
                    B[i] = A[i]
                    count += d
                else:
                    d, m = divmod(b, a+c)
                    count += d
                    B[i] = m
                flag = True
    # print(*A)
    # print(*B)
    if A != B:
        count = -1

    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)


if __name__ == '__main__':
    main()
