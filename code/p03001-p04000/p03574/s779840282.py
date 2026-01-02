#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(H: int, W: int, S: "List[str]"):
    S = [list(s) for s in S]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            counter = 0
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if k == 0 and l == 0:
                        continue
                    if i+k <= -1 or i+k >= H:
                        continue
                    if j+l <= -1 or j+l >= W:
                        continue
                    if S[i+k][j+l] == "#":
                        counter += 1
            S[i][j] = str(counter)

    print(*["".join(s) for s in S], sep="\n")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == '__main__':
    main()
