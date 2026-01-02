#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    n = 0
    d = False
    for i in range(1,len(S)+1):
        if i % 2 == 1:
            if not ( S[i-1] == "R" or 
               S[i-1] == "U" or 
               S[i-1] == "D"):
                d = True
                break
        else:
            if not ( S[i-1] == "L" or 
               S[i-1] == "U" or 
               S[i-1] == "D"):
                d = True
                break

    if d:
        print(NO)
    else:
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
