#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, M: int, A: "List[str]", B: "List[str]"):
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            found = True
            for x in range(M):
                for y in range(M):
                    if A[i + x][j + y] != B[x][y]:
                        found = False
                        break
                if not found:
                    break
            if found:
                print(YES)
                return
    print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    B = [ next(tokens) for _ in range(M) ]  # type: "List[str]"
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
