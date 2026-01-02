#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: int):
    group = []
    if S[0] == '0':
        group.append(0)
    tmp = 1
    for i in range(1, N):
        if S[i] == S[i - 1]:
            tmp += 1
        else:
            group.append(tmp)
            tmp = 1
    group.append(tmp)
    if S[-1] == '0':
        group.append(0)
    #print(group)
    num = K * 2 + 1
    if len(group) <= num:
        print(N)
        return

    cum = [0] * len(group)
    cum[0] = group[0]
    for i in range(1, len(group)):
        cum[i] = cum[i - 1] + group[i]
    cum = [0] + cum
    #print(group)
    #print(cum)

    ret = 0
    for i in range(0, len(group) - num + 1, 2):
        cumsum = cum[i + num] - cum[i]
        #print(i, i + num, cumsum)
        ret = max(ret, cumsum)
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
    S = str(next(tokens))  # type: int
    solve(N, K, S)

if __name__ == '__main__':
    main()
