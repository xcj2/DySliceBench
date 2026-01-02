#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int):
    s = 'abcdefghijkl'
    ans = []

    def f(t: str):
        if len(t) == N:
            ans.append(t)
            return
        
        if len(t) >= 2:
            x = s.index(max(list(t)))+2
        else:
            x = len(t)+1
        for i in range(x):
            f(t+s[i])


    
    f('')
    ans.sort()
    for i in ans:
        print(i)


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
