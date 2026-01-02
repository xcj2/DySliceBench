#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: str):
    rep_ss = []
    check_c = S[0]
    cnt = 0
    for char in S:
        if check_c == char:
            cnt += 1
        else:
            rep_ss.append(cnt)
            cnt = 1
            check_c = char
    rep_ss.append(cnt)
    adj = 0
    if K >= len(rep_ss)//2:
        K = len(rep_ss) // 2
        if len(rep_ss) % 2 == 0:
            K -= 1
            adj = 1
    ans = N - len(rep_ss) + 2 * K + adj
    print(ans)
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
