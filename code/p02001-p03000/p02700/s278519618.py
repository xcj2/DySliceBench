#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


YES = "Yes"  # type: str
NO = "No"  # type: str

INF=10**20
def solve(A: int, B: int, C: int, D: int):
    while True:
        C-=B
        if C <= 0:
            print(YES)
            break
        
        A-=D
        if A <= 0:
            print(NO)
            break



    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)



if __name__ == "__main__":
    main()
