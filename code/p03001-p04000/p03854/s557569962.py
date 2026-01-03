#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(S: str):
    elms = ['dream', 'dreamer', 'erase', 'eraser']
    while S:
        found = False
        for e in elms:
            if S[-len(e):] == e:
                found = True
                S = S[:-len(e)]
                break
        if not found:
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
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
