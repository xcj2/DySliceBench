#!/usr/bin/env python3
import sys


def solve(N: int, M: int, S: str):
    # dp = [float('inf')]*(N+1)
    # dp[N] = 0
    # count = 1
    # for i in range(N,-1,-1):
    #     if S[i] == "1":
    #         continue
            
    #     for j in range()
    S = S[::-1]
    cur_index = 0
    answer = []
    while True:
        for i in range(M,0,-1):
            if cur_index+i >= N:
                answer.append(N-cur_index)
                answer.reverse()
                print(*answer)
                return

            if S[cur_index+i] == "1":
                continue
            else:
                cur_index += i
                answer.append(i)
                break
        else:
            print(-1)
            return
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)
    solve(N, M, S)

if __name__ == '__main__':
    main()
