#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    if N == 0:
        if A[0] > 1:
            print(-1)
            return
        elif A[0] == 1:
            print(1)
            return

    else:
        if A[0] >= 1:
            print(-1)
            return


    for i in range(N+1):
        if A[i] > 2**i:
            print(-1)
            return
    

    safe_line = [0]*(N+1)
    safe_line[N] = A[N]
    for i in range(N-1,-1,-1):
        safe_line[i] = safe_line[i+1]+A[i]

    prev = 1
    answer = 1
    
    for i in range(1,N+1):
        cur = min(prev*2,safe_line[i])
        answer += cur
        prev = cur - A[i]
        
        if prev <= 0 and i < N:
            print(-1)
            return
        elif prev < 0 and i <= N:
            print(-1)
            return
    
    print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 0 + 1)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
