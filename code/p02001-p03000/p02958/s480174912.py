#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, p: "List[int]"):
    for i in range(N):
        if p[i] != i + 1:
            j = p[i] - 1
            p[i], p[j] = p[j], p[i]
            break
    for i in range(N):
        if p[i] != i + 1:
            print(NO)
            return
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, p)

if __name__ == '__main__':
    main()
