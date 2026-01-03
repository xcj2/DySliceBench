#!/usr/bin/env python3
import sys
# from collections import Counter

def solve(s: str):
    alpha_list = set(s)

    answer = 10**9
    for alpha in alpha_list: #全部をalphaにする
        S = s
        count = 0
        while len(set(S)) > 1:
            new_S = ""
            
            for i in range(len(S)-1):
                if S[i] == alpha or S[i+1] == alpha:
                    new_S += alpha
                else:
                    new_S += "@"
            S = new_S
            count += 1
        answer = min(answer,count)

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
