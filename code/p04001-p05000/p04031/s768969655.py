#!/usr/bin/env python3
import sys
import numpy as np

def solve(N: int, a: "List[int]"):
    a_num = np.array(a)
    min_value = np.min(a_num)
    max_value = np.max(a_num)

    answer = 10**7
    for i in range(min_value,max_value+1):
        goal = np.full(N,i)
        dif = a_num-goal
        nijo = dif**2
        answer = min(answer,np.sum(nijo))
    print(int(answer))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
