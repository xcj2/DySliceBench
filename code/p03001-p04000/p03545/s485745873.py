#!/usr/bin/env python3
import sys
import itertools

def solve(ABCD: str):
    A, B, C, D = map(int,ABCD)
    bit_list = list(itertools.product(["+","-"], repeat=3))
    for bit in bit_list:
        a=A
        if bit[0] == "+":
            a+=B
        else:
            a-=B        
        if bit[1] == "+":
            a+=C
        else:
            a-=C        
        if bit[2] == "+":
            a+=D
        else:
            a-=D    
        if a == 7:
            print("{}{}{}{}{}{}{}=7".format(A,bit[0],B,bit[1],C,bit[2],D))
            break 

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    ABCD = next(tokens)  # type: int
    solve(ABCD)

if __name__ == '__main__':
    main()
