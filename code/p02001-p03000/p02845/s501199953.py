#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    if A[0] != 0:
        print(0)
        return 

    ## 一番多い色の帽子の数
    color = [1,0,0]
    answer = 3

    for i in range(1,N):
        if A[i] not in color:
            print(0)
            return 
        
        count = color.count(A[i])
        answer *= count

        for j in range(len(color)):
            if color[j] == A[i]:
                color[j]+=1
                break

    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
