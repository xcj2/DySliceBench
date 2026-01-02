#!/usr/bin/env python3
import sys


def solve(S: str):
    answer = 0
    if len(S)%2 == 0:
        half  = len(S)//2
        for i in range(half,len(S)):
            if S[i] != S[len(S)-i-1]:
                answer += 1
    else:
        half  = len(S)//2
        for i in range(half+1,len(S)):
            if S[i] != S[len(S)-i-1]:
                answer += 1     
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
