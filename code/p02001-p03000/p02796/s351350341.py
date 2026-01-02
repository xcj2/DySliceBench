#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, X: "List[int]", L: "List[int]"):
    s = [X[i]-L[i] for i in range(N)]
    e = [X[i]+L[i] for i in range(N)]
    se = [[s[i],e[i]] for i in range(N)]
    se = sorted(se, key=lambda x:x[1])

    ans = [se[0]]

    for i in range(1, N):
        if se[i][0] < ans[-1][1]:
            continue
        else:
            ans.append(se[i])

    # print(ans)
    print(len(ans))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    L = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        L[i] = int(next(tokens))
    solve(N, X, L)

if __name__ == '__main__':
    main()
