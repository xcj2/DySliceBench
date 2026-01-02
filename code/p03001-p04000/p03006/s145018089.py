#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[int]", y: "List[int]"):
    diffs = []
    for i in range(N):
        for j in range(i + 1, N):
            diffs.append([x[j] - x[i], y[j] - y[i]])
            diffs.append([x[i] - x[j], y[i] - y[j]])
    diffs.sort()
    cnt = 0
    tmp = 1
    for i in range(1, len(diffs)):
        if diffs[i] == diffs[i - 1]:
            tmp += 1
        else:
            cnt = max(tmp, cnt)
            tmp = 1
    ret = N - cnt
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]" 
    y = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()
