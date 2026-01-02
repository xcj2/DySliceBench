#!/usr/bin/env python3
import sys

def solve(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    SA=[[0]*W for i in range(H)]
    MAX = (H+W)*80
    for i in range(H):
        for j in range(W):
            SA[i][j]=abs(A[i][j]-B[i][j])

    DP=[[0 for i in range(W)] for j in range(H)]
    DP[0][0]=1<<MAX+SA[0][0]

    for i in range(H):
        for j in range(W):
            tempbit=DP[i][j]
            if i<H-1:
                DP[i+1][j]|=tempbit<<SA[i+1][j]
                DP[i+1][j]|=tempbit>>SA[i+1][j]

            if j<W-1:
                DP[i][j+1]|=tempbit<<SA[i][j+1]
                DP[i][j+1]|=tempbit>>SA[i][j+1]

    ANS=1<<MAX*2
    for i in range(MAX*2+1):
        if 1<<i & DP[-1][-1]!=0:
            ANS=min(ANS,abs(i-MAX))

    print(ANS)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A, B)

if __name__ == '__main__':
    main()
