#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    tmp = [[False] * 3 for _ in range(3)]
    for i, vals in enumerate(A):
        for j, v in enumerate(vals):
            if v in b:
                tmp[i][j] = True
    for i in range(3):
        found = True
        for j in range(3):
            if not tmp[i][j]:
                found = False
        if found:
            print(YES)
            return
    for i in range(3):
        found = True
        for j in range(3):
            if not tmp[j][i]:
                found = False
        if found:
            print(YES)
            return
    if tmp[0][0] and tmp[1][1] and tmp[2][2]:
        print(YES)
        return
    if tmp[0][2] and tmp[1][1] and tmp[2][0]:
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
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
