#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, A: "List[int]", B: "List[int]"):
    p = []
    for i in range(N):
        p.append([A[i], B[i]])
    p.sort(key=lambda x: x[1])
    tmp = 0
    ret = YES
    for i in range(N):
        tmp += p[i][0]
        if tmp > p[i][1]:
            ret = NO
            break
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]" 
    B = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
