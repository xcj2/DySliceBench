#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, K: int, A: "List[int]"):
    ## 一つの場合の転倒数を数えていく
    tentousuu = dict()
    all_tentousuu = dict()
    for a in range(0,2001):
        tentousuu[a] = 0
        all_tentousuu[a] = 0 

    for i in range(0,N):
        for j in range(0,N):
            if j<i and A[j]>A[i]:
                tentousuu[A[i]]+=1
            
            if A[i]<A[j]:
                all_tentousuu[A[i]] += 1
    
    one_to_k_sum = (K)*(K-1)//2
    answer = 0
    for a in range(0,2001):
        answer += tentousuu[a]*K+all_tentousuu[a]*one_to_k_sum
    
    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
