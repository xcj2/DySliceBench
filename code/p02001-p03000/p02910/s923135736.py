#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    ret = YES
    for i in range(len(S)):
        if i % 2 == 0 and S[i] in ['R', 'U', 'D']:
            continue
        if i % 2 == 1 and S[i] in ['L', 'U', 'D']:
            continue
        ret = NO
        break
    print(ret)
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
