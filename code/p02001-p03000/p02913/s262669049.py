#!/usr/bin/env python3
import sys

def z_algo(S):
    N = len(S)
    LCPs = [0]*N
    i = 1 ## iから何文字一致してるか調べる
    j = 0
    LCPs[0] = N
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        if j == 0:
            i += 1
            continue
        LCPs[i] = j
        k = 1
        while k+i < N and k+LCPs[k] < j:
            LCPs[i+k] = LCPs[k]
            k += 1
        i += k
        j -= k
    return LCPs

def solve(N: int, S: str):
    answer = 0
    for i in range(N):
        LCP = z_algo(S[i:])
        for j in range(len(LCP)):
            # jの長さまでなら重ならない
            a = min(j,LCP[j])
            answer = max(answer,a)
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
