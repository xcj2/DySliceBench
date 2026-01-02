#!/usr/bin/env python3
import sys

def solve(N: int, X: int):
    # amount[i] = level iバーガーのP+Bの総数
    amount = [0]*N
    amount[0] = 5
    for i in range(N-1):
        amount[i+1] = amount[i]*2 + 3

    # amount[i] = level iバーガーのPの総数
    p_amount = [0]*N
    p_amount[0] = 3

    for i in range(N-1):
        p_amount[i+1] = p_amount[i]*2 + 1
    
    # レベルNバーガーの下からX個に含まれるPの個数を返す
    def dfs(n,x) -> int:
        if x == 0:
            return 0
            
        if n == 1:
            if x == 1 or x == 0:
                return 0
            elif 2<= x <= 4:
                return x-1
            else:
                return 3


        half = (amount[n-1]-3)//2 + 1
        if x <= half:
            return dfs(n-1,x-1)
        else:
            res = x-half-1
            return p_amount[n-2]+1+dfs(n-1,res)
    
    print(dfs(N,X))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(N, X)

if __name__ == '__main__':
    main()
