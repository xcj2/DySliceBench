#!/usr/bin/env python3
import sys


def solve(X: int):
    i = 2
    vals = [1]
    while i * i <= X:
        tmp = i
        while tmp <= X:
            #print(tmp)
            vals.append(tmp)
            tmp *= i
        i += 1
    vals.sort()
    ret = vals[-1]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
