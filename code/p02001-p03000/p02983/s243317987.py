#!/usr/bin/env python3
import sys

MOD = 2019  # type: int

def solve(L: int, R: int):
    if R-L >= 2018:
        print(0)
        return 
    
    lr_all = list(range(L,R+1))
    answer = 2019
    for i in range(R-L+1):
        for j in range(i+1,R-L+1):
            answer = min(lr_all[i]*lr_all[j]%MOD,answer)
    
    print(answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)

if __name__ == '__main__':
    main()
