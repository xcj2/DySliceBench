#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(S: str):
    S = S[::-1]
    while len(S)>4:
        if S[:6]=="resare":
            S= S[6:]
        elif S[:5] == "esare" or S[:5]== "maerd":
            S=S[5:]
        elif S[:7] == "remaerd":
            S=S[7:]
        else:
            print(NO)
            return 
        
    
    if len(S) == 0:
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

