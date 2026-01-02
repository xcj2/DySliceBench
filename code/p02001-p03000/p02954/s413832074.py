#!/usr/bin/env python3
import sys, math, fractions, itertools


def solve(S: str):
    c = 'R'
    ci = 0
    counter = 1
    S += 'R'
    A = [0] * len(S)

    for i, s in enumerate(S):
        if i == 0:
            continue
        if s == 'R' and c == 'R':
            counter += 1
        elif (s == 'L' or i == len(S)-1) and c == 'R':
            if counter % 2 == 0:
                A[i] += counter // 2
                A[i-1] += counter // 2
            else:
                A[i] += (counter-1) // 2
                A[i-1] += (counter+1) // 2
            counter = 1
            ci = i
            c = 'L'
        elif (s == 'R' or i == len(S) - 1) and c == 'L':
            if counter % 2 == 0:
                A[i-counter-1] += counter // 2
                A[i-counter] += counter // 2
            else:
                A[i-counter-1] += (counter-1) // 2
                A[i-counter] += (counter+1) // 2
            counter = 1
            ci = i
            c = 'R'
        elif s == 'L' and c == 'L':
            counter += 1
    print(' '.join([str(a) for a  in A[:-1]]))
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
