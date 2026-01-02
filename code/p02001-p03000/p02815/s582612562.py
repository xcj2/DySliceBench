#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, C: "List[int]"):
    if N == 1:
        print(2*C[0]%MOD)
        return
    
    start = pow(2,N-1,MOD)
    distance = pow(2,N-2,MOD)

    count = [0]*N
    for i in range(N):
        count[i] = (start+distance*i)%MOD
    answer = 0
    C.sort(reverse=True)
    for i in range(N):
        answer += C[i]*count[i]
        answer%=MOD
    answer*=pow(2,N,MOD)
    answer%=MOD
    print(answer)


    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C)

if __name__ == '__main__':
    main()
