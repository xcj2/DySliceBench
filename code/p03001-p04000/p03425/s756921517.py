#!/usr/bin/env python3
import sys
from itertools import product

def solve(N: int, S: "List[str]"):
    answer = 0
    march_dict = {'M':0,'A':0,'R':0,'C':0,'H':0}
    for i in range(N):
        if march_dict.get(S[i][0]) != None:
            march_dict[S[i][0]] += 1
    values = list(march_dict.values())
    bit_list = product([0,1],repeat=5)

    for bit in bit_list:
        if bit.count(1) == 3:
            a = 1
            for i in range(5):
                if bit[i] == 1:
                    a *= values[i]
            answer += a

    print(answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
