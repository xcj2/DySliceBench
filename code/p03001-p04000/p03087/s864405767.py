#!/usr/bin/env python3
import sys


def solve(n: int, Q: int, S: str, l: "List[int]", r: "List[int]"):
    count = [0] * (n + 1)
    tmp = 0
    for idx in range(n - 1):
        if S[idx:idx + 2] == 'AC':
            tmp += 1
        count[idx + 1] = tmp
    #print(count)
    for i in range(Q):
        ret = count[r[i] - 1] - count[max(0, l[i] - 2)]
        if l[i] > 1 and S[l[i] - 2:l[i]] == 'AC':
            ret -= 1
        print(ret)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    l = [int()] * (Q)  # type: "List[int]" 
    r = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, S, l, r)

if __name__ == '__main__':
    main()
