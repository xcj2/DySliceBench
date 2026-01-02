#!/usr/bin/env python3
import sys

def solveChild(S: str, start: int, N: int):
    # return the final position of this child after 10^100 times moves
    # same == 1: stop at same as start
    # same == 0: stop at different with starts
    if S[start] == 'L':
        i = start - 1
        for i in range(start - 1, -1, -1):
            if S[i] == 'R':
                lastL = i+1
                # firstR = i
                break
        if (start - lastL) % 2 == 1: # start - lastL is odd
            same = False
            return lastL - 1, same
        else: # start - lastL is even
            same = True
            return lastL, same
    else: # S[start] == 'R'
        for i in range(start + 1, N):
            if S[i] == 'L':
                lastR = i - 1
                # firstL = i
                break
        if (lastR - start) % 2 == 1: # start - lastR is odd
            same = False
            return lastR + 1, same
        else: # start - lastR is even
            same = True
            return lastR, same

def solve(S: str):
    N = len(S)
    num_child = [0] * N
    # first 
    stop, same = solveChild(S, 0, N)
    num_child[stop] += 1
    for start in range(1, N):
        if S[start] == 'L' and S[start - 1] == 'L':
            if same:
                stop -= 1
                num_child[stop] += 1
                same = False
            else:
                stop += 1
                num_child[stop] += 1
                same = True
        elif S[start] == 'R' and S[start - 1] == 'R':
            if same:
                stop += 1
                num_child[stop] += 1
                same = False
            else:
                stop -= 1
                num_child[stop] += 1
                same = True
        else:
            stop, same = solveChild(S, start, N)
            num_child[stop] += 1

    print(' '.join(map(str, num_child)))
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
