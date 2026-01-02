#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, K: int, x: "List[int]", y: "List[int]"):
    answer = 10**19

    x_set = sorted(list(set(x)))
    y_set = sorted(list(set(y)))
    x_combination = list(itertools.combinations(x_set,2))
    y_combination = list(itertools.combinations(y_set,2))

    
    for x_l, x_u in x_combination:
        for y_l, y_u in y_combination:
            count = 0
            for i in range(N):
                if y_l <= y[i] <= y_u and x_l <= x[i] <= x_u:
                    count +=1
            if count >= K:
                answer = min(answer,(y_u-y_l)*(x_u-x_l))

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, K, x, y)

if __name__ == '__main__':
    main()
