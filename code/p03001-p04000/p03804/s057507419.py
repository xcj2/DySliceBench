#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[str]", B: "List[str]"):
    for i in range(N-M+1):
        for j in range(N-M+1):
            # AとBが等しいか判定
            for k in range(M):
                for l in range(M):
                    if A[i+k][j+l] == B[k][l]:
                        continue
                    else:
                        break
                else:
                    continue
                break    
            else:
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
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    B = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
