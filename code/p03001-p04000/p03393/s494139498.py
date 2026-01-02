#!/usr/bin/env python3
import sys

def solve(S: str):
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
        return

    if len(S) < 26:
        res = sorted(list(set("zyxwvutsrqponmlkjihgfedcba")-set(S)))
        print(S+res[0])
    else:
        prev = None
        for i in range(25,-1,-1):
            if prev == None or prev < S[i]:
                prev = S[i]
                continue
            else:
                res = sorted(list(set("zyxwvutsrqponmlkjihgfedcba")-set(S[:i+1])))
                for s in res:
                    if s > S[i]:
                        print(S[:i]+s)
                        return
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
