#!/usr/bin/env python3
import sys


def solve(N: int, s: "List[int]"):
    mod = [s[i]%10 for i in range(N)]
    if sum(mod)%10!=0:
        print(sum(s))
        return 
    
    s.sort()
    for ss in s:
        if ss%10!=0:
            print(sum(s)-ss)
            return 
    
    print(0)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, s)

if __name__ == '__main__':
    main()
