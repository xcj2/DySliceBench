#!/usr/bin/env python3
import sys


def solve(S: str, K: int):
    S = list(map(lambda c:int(c), S))
    for i in range(len(S)):
        #print("i = {}".format(i))
        if S[i] == 1 and i+1 == K:
            print(1)
            break
        elif S[i] != 1:
            print(S[i])
            break
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(S, K)

if __name__ == '__main__':
    main()
