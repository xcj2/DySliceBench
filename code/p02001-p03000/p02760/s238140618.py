#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    
    line = [a for a in A]
    
    line.append([A[i][0] for i in range(3)])
    line.append([A[i][1] for i in range(3)])
    line.append([A[i][2] for i in range(3)])
    line.append([A[0][0], A[1][1], A[2][2]])
    line.append([A[0][2], A[1][1], A[2][0]])

    #print(line)
    #print(b)
    for Al in line:
        #print(Al)
        if len(set(b) & set(Al)) == 3:
            print(YES)
            sys.exit()
    print(NO)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
