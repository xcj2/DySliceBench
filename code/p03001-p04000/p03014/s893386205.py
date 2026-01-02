#!/usr/bin/env python3
import sys

def solve(H: int, W: int, S: "List[str]"):
    ss = [list(s) for s in S]
    answer = 0
    right = [[0]*W for _ in range(H)]
    left = [[0]*W for _ in range(H)]
    up = [[0]*W for _ in range(H)]
    down = [[0]*W for _ in range(H)]

    for h in range(H):
        for j in range(W):
            if ss[h][j] == ".":
                if j>0:
                    right[h][j] = 1+right[h][j-1]
                else:
                    right[h][j] += 1
            else:
                right[h][j] = 0

        for j in range(W-1,-1,-1):
            if ss[h][j] == ".":
                if j<W-1:
                    left[h][j] = 1+left[h][j+1]
                else:
                    left[h][j] += 1
            else:
                left[h][j] = 0
    for w in range(W):                
        for i in range(H-1,-1,-1):
            if ss[i][w] == '.':
                if i < H-1:
                    up[i][w] = 1 + up[i+1][w]
                else:
                    up[i][w] +=1
            else:
                up[i][w] = 0
        for i in range(0,H):
            if ss[i][w] == '.':
                if i > 0:
                    down[i][w] = 1 + down[i-1][w]
                else:
                    down[i][w] +=1
            else:
                down[i][w] = 0

    for i in range(H):
        for j in range(W):
            answer = max(answer,right[i][j]+left[i][j]+up[i][j]+down[i][j]-3)

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)

if __name__ == '__main__':
    main()
