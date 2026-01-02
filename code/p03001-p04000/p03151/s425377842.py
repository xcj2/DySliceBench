#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]", B: "List[int]"):

    enough = []
    husoku = 0
    counter = 0
    for a, b in zip(A, B):
        if a < b:
            husoku += b-a
            counter += 1
        else:
            enough.append(a-b)
    enough.sort(reverse=True)
    i = 0
    while husoku > 0 and i < len(enough):
        husoku -= enough[i]
        counter += 1
        i += 1

    if husoku > 0:
        print(-1)
    else:
        print(counter)
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
