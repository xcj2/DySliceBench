#!/usr/bin/env python3
import sys
from itertools import product
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    H,W,K = MAP()
    S = [input() for _ in range(H)]
    accum_s = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if j == 0:
                accum_s[i][j] = int(S[i][j])
            else:
                accum_s[i][j] = accum_s[i][j-1]+int(S[i][j])

    answer = 10**9
    for p in product([0,1],repeat=H-1):
        one_index = [i for i in range(H-1) if p[i] == 1]
        one_index.append(H-1)
        score = 0
        prev_j = -1
        outflag = False

        for j in range(W):
            if outflag:
                break
            prev_i = 0
            for slice_index in one_index:
                group_count = 0
                
                while prev_i <= slice_index:
                    if prev_j == -1:
                        group_count += accum_s[prev_i][j]
                    else:
                        group_count += accum_s[prev_i][j] - accum_s[prev_i][prev_j]

                    prev_i += 1
                
                if group_count > K:
                    if prev_j == j-1:
                        outflag = True
                    score += 1
                    prev_j = j-1
                    break
        else:
            if answer > score+len(one_index)-1:
                answer = score+len(one_index)-1
    
    print(answer)


if __name__ == '__main__':
    main()
