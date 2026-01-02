#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, S: str):
    ret = 0
    cnt = 1
    tmp = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            if cnt > 1:
                ret += cnt - 1
            cnt = 1
            tmp += 1
    ret += cnt - 1
    ret += min(K, tmp // 2) * 2
    if K > tmp // 2:
        ret += tmp % 2
    ret = min(ret, N - 1)
    print(ret)
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
