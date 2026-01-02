#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, D: "List[int]", M: int, T: "List[int]"):
    
    D.sort()
    T.sort()

    from bisect import bisect_left, bisect_right

    if M > N:
        print(NO)
        exit()


    for i in range(M):
        lf = bisect_left(D, T[i])
        ri = bisect_right(D, T[i])
        if lf != ri:
            D[lf] = 0
        else:
            print(NO)
            exit()

    print(YES)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, D, M, T)

if __name__ == '__main__':
    main()
