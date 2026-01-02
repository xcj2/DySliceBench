#!/usr/bin/env python3
import sys


def solve(N: int):
    memo = [[0]*10 for _ in range(10)]

    for num in range(1,N+1):
        s_num = str(num)
        memo[int(s_num[0])][int(s_num[-1])] += 1
    
    answer = 0
    for i in range(10):
        for j in range(10):
            answer += memo[i][j]*memo[j][i]
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
