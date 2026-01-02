#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    # リーダーの方を向く人数＝リーダーより左のWの数＋リーダーより右のEの数
    accum_W = [0]*N #iより左にWが何個あるか
    accum_E = [0]*N #iよりみぎにEが何個あるか

    for i in range(1,N):
        accum_W[i] = accum_W[i-1]+int(S[i-1]=="W")

    for i in range(N-2,-1,-1):
        accum_E[i] = accum_E[i+1] + int(S[i+1] == "E")
    
    answer = N
    for i in range(N):
        a = accum_W[i]+accum_E[i]
        answer = min(answer,a)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
