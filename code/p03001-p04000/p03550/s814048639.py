#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

def solve(N: int, Z: int, W: int, a: "List[int]"):
    # memo[i][j] = 手番がi(X:0,Y:1)のときすでにj-index引いてる
    memo = [[0]*N for _ in range(2)]

    def maxValue(z:int, w:int, i: int, player:str) -> int:
        if i >= N:
            return abs(z-w)

        if player == "X": ## playerXが操作する。価値がmaxになるように
            if memo[0][i] > 0:
                return memo[0][i]

            value = 0
            for j in range(i,N):
                value = max(maxValue(a[j],w,j+1,"Y"),value)
            memo[0][i] = value
        else: ## yが操作,価値がminになるように
            if memo[1][i] > 0:
                return memo[1][i]
            value = 10**9
            for j in range(i,N):
                value = min(maxValue(z,a[j],j+1,"X"),value)
            memo[1][i] = value

        return value        

    print(maxValue(Z,W,0,"X"))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, Z, W, a)

if __name__ == '__main__':
    main()
