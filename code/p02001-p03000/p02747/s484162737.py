#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    length = len(S)
    if length % 2 != 0:
        print(NO)
        return
    
    for i in range(length):
        if i % 2 == 0 and S[i] != "h":
            print(NO)
            return
        elif i % 2 != 0 and S[i] != "i":
            print(NO)
            return

    print(YES)

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
