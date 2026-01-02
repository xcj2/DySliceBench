#!/usr/bin/env python3
import sys

def solve(N: int, C: int, x: "List[int]", v: "List[int]"):
    l_cum = [[0, 0] for _ in range(N + 1)]
    r_cum = [[0, 0] for _ in range(N + 1)]
    cal = 0
    for i in range(N):
        cal += v[i]
        val = cal - x[i]
        if val > l_cum[i][0]:
            l_cum[i + 1] = [val, x[i]]
        else:
            l_cum[i + 1] = l_cum[i]
    cal = 0
    for i in range(N - 1, -1, -1):
        cal += v[i]
        pos = C - x[i]
        val = cal - pos
        if val > r_cum[i + 1][0]:
            r_cum[i] = [val, pos]
        else:
            r_cum[i] = r_cum[i + 1]
    #print(l_cum)
    #print(r_cum)
    ret = 0
    for i in range(N + 1):
        ret = max(ret, l_cum[i][0] + r_cum[i][0] - min(l_cum[i][1], r_cum[i][1]))
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]" 
    v = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        x[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, C, x, v)

if __name__ == '__main__':
    main()
