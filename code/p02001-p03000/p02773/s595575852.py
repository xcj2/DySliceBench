#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    
    word = {}

    for s in S:
        if s not in word.keys():
            word[s] = 1
        else:
            word[s] = word[s] + 1

    max_n = max(word.values())

    max_w = [key for key in word.keys() if word[key] == max_n]

    max_w.sort()

    for st in max_w:
        print(st)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
