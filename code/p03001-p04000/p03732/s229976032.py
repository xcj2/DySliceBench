#!/usr/bin/env python3
import sys
from itertools import accumulate
def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    value = {}
    value[w[0]] = []
    value[w[0]+1] = []
    value[w[0]+2] = []
    value[w[0]+3] = []
    accum = {}
    answer = 0

    for i in range(N):
        value[w[i]].append(v[i])

    len0 = len(value[w[0]])
    len1 = len(value[w[0]+1])
    len2 = len(value[w[0]+2])
    len3 = len(value[w[0]+3])

    for i in range(4):
        value[w[0]+i].sort(reverse = True)
        accum[w[0]+i] = [0]+list(accumulate(value[w[0]+i]))

    for i in range(len0+1):
        for j in range(len1+1):
            for k in range(len2+1):
                for l in range(len3+1):
                    if i*w[0]+j*(w[0]+1)+k*(w[0]+2)+l*(w[0]+3) <= W:
                        answer = max(accum[w[0]][i]+accum[w[0]+1][j]+accum[w[0]+2][k]+accum[w[0]+3][l],answer)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)

if __name__ == '__main__':
    main()
