#!/usr/bin/env python3
import sys
import itertools

def solve(N: int):
    string = "abcdefghijk"
    if N == 1:
        print("a")
        return


    answer = []
    def dfs(s,various):
        if len(s) == N:
            return s
        new = dfs(s+string[various],various+1)
        if new:
            answer.append(new)

        for i in range(various):
            n = dfs(s+string[i],various)
            if n:
                answer.append(n)

    dfs("a",1)
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
