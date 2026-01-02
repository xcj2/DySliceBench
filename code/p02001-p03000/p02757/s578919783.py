#!/usr/bin/env python3
import sys


def solve(N: int, P: int, S: str):
    if P == 2 or P ==5:
        answer = 0
        for i in range(N):
            if int(S[i])%P == 0:
                answer += i+1
        print(answer)
        return

    amari = [0]*N
    amari[N-1] = int(S[N-1])%P
    keta = 1
    for i in range(N-2,-1,-1):
        num = pow(10,keta,P)*int(S[i])
        amari[i]=(amari[i+1]+num)%P
        keta += 1
    from collections import Counter
    counter = Counter(amari)
    answer = 0
    for _,value in counter.items():
        answer += (value*(value-1))//2
    answer += amari.count(0)
    print(answer)  
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = next(tokens)  # type: int
    solve(N, P, S)

if __name__ == '__main__':
    main()
