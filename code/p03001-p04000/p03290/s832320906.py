#!/usr/bin/env python3
import sys, math, fractions, itertools


def solve(D: int, G: int, p: "List[int]", c: "List[int]"):
    mn = 1e5
    for i in range(1 << D):
        score = 0
        count = 0
        for j in range(D):
            if i >> j & 1 == 1:
                score += p[j] * 100 * (j+1) + c[j]
                count += p[j]
        if score >= G:
            mn = min(mn, count)
            continue
        for k in range(D):
            j = D - k - 1
            if i >> j & 1 == 0:
                if score + 100*(j+1)*(p[j]-1) >= G:
                    count += math.ceil((G - score) / (100*(j+1)))
                    score += 100*(j+1)*count
                    break
                else:
                    score += 100*(j+1)*(p[j]-1)
                    count += p[j] - 1
        # print(score, count)
        if score >= G:
            mn = min(mn, count)
    print(mn)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    p = [int()] * (D)  # type: "List[int]" 
    c = [int()] * (D)  # type: "List[int]" 
    for i in range(D):
        p[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(D, G, p, c)

if __name__ == '__main__':
    main()
