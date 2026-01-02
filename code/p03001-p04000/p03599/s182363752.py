#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int, E: int, F: int):
    A_enable = []
    B_enable = []
    AB_enable = []
    a = 0
    while a <= F:
        A_enable.append(a)
        a += A*100
    
    b = 0
    while b <= F:
        B_enable.append(b)
        b += B*100

    for aa in A_enable:
        for bb in B_enable:
            if aa+bb<=F:
                AB_enable.append(aa+bb)
    AB_enable = sorted(list(set(AB_enable)))
    AB_enable.pop(0)

    C_enable = []
    D_enable = []
    CD_enable = []
    c = 0
    while c <= F:
        C_enable.append(c)
        c += C
    d = 0
    while d <= F:
        D_enable.append(d)
        d += D

    for cc in C_enable:
        for dd in D_enable:
            if cc+dd <= F:
                CD_enable.append(cc+dd)
    CD_enable = sorted(list(set(CD_enable)))
    CD_enable.pop(0)

    answer = [AB_enable[0],0,0] 

    for aabb in AB_enable:
        for ccdd in CD_enable:
            if (aabb/100)*E >= ccdd and aabb+ccdd<=F and answer[2] < ccdd/(aabb+ccdd): 
                
                answer[0] = aabb
                answer[1] = ccdd
                answer[2] = ccdd/(aabb+ccdd)
    
    print(answer[0]+answer[1], answer[1])
            
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F)

if __name__ == '__main__':
    main()
