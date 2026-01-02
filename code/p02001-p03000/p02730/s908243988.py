#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True    

def solve(S: str):
    all = is_kaibun(S)
    zenhan = is_kaibun(S[:len(S)//2])
    kouhan = is_kaibun(S[len(S)//2+1:])
    if all and zenhan and kouhan:
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
