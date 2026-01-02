#!/usr/bin/env python3
import sys
from pprint import pprint
 
def solve(H: int, W: int, A: "List[str]"):
    count = [[H + W] * (W + 2) for _ in range(H + 2)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                count[i + 1][j + 1] = 0
            else:
                count[i + 1][j + 1] = min(count[i][j + 1], count[i + 1][j]) + 1
 
    #pprint(count)
    ret = 0
    for i in range(H, 0, -1):
        for j in range(W, 0, -1):
            count[i][j] = min(count[i][j], min(count[i][j + 1], count[i + 1][j]) + 1)
            ret = max(ret, count[i][j])
    #pprint(count)
    print(ret)
    return
 
 
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, A)
 
if __name__ == '__main__':
    main()