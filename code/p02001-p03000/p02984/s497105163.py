#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]"):

    # ax+b
    xlist = [[1,0]]+[[] for _ in range(N)]
    for i in range(N):
        a = 0-xlist[i][0]
        b = A[i]*2-xlist[i][1]
        xlist[i+1]=[a,b]
    
    first = xlist[0]
    last = xlist[-1]
    a = first[0]-last[0]
    b = first[1]-last[1]
    x = -b//a

    answer = []
    for i in range(N):
        a = xlist[i][0]
        b = xlist[i][1]
        answer.append(a*x+b)
    
    print(*answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
