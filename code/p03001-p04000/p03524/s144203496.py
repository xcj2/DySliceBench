#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(S: str):
    N = len(S)
    l = list(S)

    from collections import Counter
    c = Counter(l)
    
    if(abs(c['a']-c['b']) <= 1 and abs(c['b']-c['c']) <= 1 and abs(c['c']-c['a']) <= 1):
        print(YES)
    else:
        print(NO)

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
