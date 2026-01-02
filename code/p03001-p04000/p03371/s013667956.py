#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    # > なお、ピザの組み替えにより、必要な量を超えたピザが発生しても構いません。
    val_min = 5001 * (X+Y)
    for z in range(0, 2*max(X, Y)+1, 2):
        x = max(0, X - z//2)
        y = max(0, Y - z//2) 
        val_min_cond = A*x + B*y + C*z
        #print(x,y,z,val_min_cond)
        val_min = val_min_cond if val_min_cond < val_min else val_min
    print(val_min)
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
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(A, B, C, X, Y)

if __name__ == '__main__':
    main()
