#!/usr/bin/env python3
import sys

def solve(N: int, S: str):

    a = ""
    ans = 0
    for i in range(N):
        a += S[i]
        while(len(a) > 0):
            if a in S[i+1:]:    
                ans = max(ans,len(a))
                break
            else:               
                a = a[1:]
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
