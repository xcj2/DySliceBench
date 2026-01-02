#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(S: str):
    # print(''.join(S.split('A')))
    if ''.join(S.split('A')) == "KIHBR":
        if 'AA' not in S and 'KIH' in S:
            print(YES)
            exit()
    
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
