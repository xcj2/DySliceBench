#!/usr/bin/env python3
import sys


def solve(T: "List[int]", A: "List[int]", B: "List[int]"):
    dif1 = T[0]*(A[0] - B[0])
    dif2 = T[1]*(A[1] - B[1])

    if dif1+dif2 == 0:
        print('infinity')
        return
    
    if dif1*dif2>0 or abs(dif1)>abs(dif2):
        print(0)
        return
    
    ## tが抜かれる方
    t = abs(dif1)
    a = abs(dif2)

    if t%abs(t-a)==0:
        print(2*(t//abs(t-a)))
    else:
        print(2*(t//abs(t-a))+1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    A = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    solve(T, A, B)

if __name__ == '__main__':
    main()
