#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, A: int, B: int, S: str):

    b = [1 if S[i]=='b' else 0 for i in range(N)]
    lb = [0] * (N+1)
    for i in range(N):
        lb[i+1] = lb[i] + b[i]


    cnt = 0
    for i in range(N):
        if S[i] == 'c':
            print(NO)
        
        elif cnt < A+B:
            if S[i] == 'a':
                print(YES)
                cnt += 1
        
            elif S[i] == 'b' and lb[i] < B:
                print(YES)
                cnt += 1
        
            else:
                print(NO)

        else:
            print(NO)
        

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, A, B, S)

if __name__ == '__main__':
    main()
