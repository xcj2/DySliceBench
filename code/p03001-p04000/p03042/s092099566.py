#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(S: str):
    u = int(S[:2])
    d = int(S[2:])
    
    if 0 < u <= 12 and 0 < d <= 12:
        print('AMBIGUOUS')
    
    elif 0 < d <= 12:
        print('YYMM')

    elif 0 < u <= 12:
        print('MMYY')
        
    else:
        print('NA')
        
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()
