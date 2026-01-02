#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, S: "List[str]"):

    A = 0
    count = 0
    for B in range(N):
        # print("***", B)
        flag = True
        # for i in range(N):
        #     print(S[i][B:]+S[i][:B])
        for i in range(N):
            for j in range(i, N):
                # print(i, j, j-B, S[i][j-B], S[j][i-B])
                if S[i][j-B] != S[j][i-B]:
                    flag = False
                    break
            if flag is False:
                break
        if flag:
            count += 1
    print(count*N)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
