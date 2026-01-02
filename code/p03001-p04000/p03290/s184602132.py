#!/usr/bin/env python3
import sys
from math import ceil

def solve(D: int, G: int, p: "List[int]", c: "List[int]"):
    answer = 1000
    ## どの問題を全部解くか全探索
    for i in range(2**D):
        tmpans = 0
        score = 0
        com_problem = []

        for j in range(D):
            if i & 1<<j:
                score += p[j]*100*(j+1)+c[j]
                tmpans += p[j]
                com_problem.append(j)
        if score >= G:
            answer = min(answer,tmpans)
        else:

            for probrem_index in range(D-1,-1,-1):
                if probrem_index in com_problem:
                    continue

                if (G-score)>100*(probrem_index+1)*(p[probrem_index]-1):
                    break
                else:
                    tmpans += ceil((G-score) / (100*(probrem_index+1)))
                    answer = min(answer,tmpans)
                    break

    print(answer)

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
