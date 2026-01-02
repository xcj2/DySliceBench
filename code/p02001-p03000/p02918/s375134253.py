#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, S: str):

    seq = []
    ans = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
        else:
            seq.append(ans)
            ans = 1
    # 最後
    if S[N-2] == S[N-1]:
        seq.append(ans)
    else:
        seq.append(1)
    # print(seq)

    if len(seq) - 2*K <= 1:
        print(N-1)
    else:
        ans = 0
        for c in seq:
            ans += c-1
        print(ans+2*K)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)


if __name__ == '__main__':
    main()
