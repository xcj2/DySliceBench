from sys import stdin
import math
import itertools


def makeIntMatrix(lines):
    intMatrix = []
    for a in makeStringMatrix(lines):
        intMatrix.append([int(b) for b in a])
    return intMatrix
 
 
def makeStringMatrix(lines):
    stringMatrix = [line.split() for line in lines]
    return stringMatrix
 
 
def makeInt(line):
    return int(line.rstrip())
 
 
def makeMultiInteger(line):
    return [int(x) for x in line.rstrip().split()]


def solve(input_string):
    N, M = makeMultiInteger(input_string[0])
    S = makeIntMatrix(input_string[1:])
    c = 0
    ra = range(1, N+1)
        
    min_range = ra
    min_l = ra[0]
    min_r = ra[-1]
    for s in S:
        l = s[0]
        r = s[1]
        if l > min_range[0]:
            min_l = l
        if r < min_range[-1]:
            min_r = r
        min_range = range(min_l, min_r+1)
        if len(min_range) == 0:
            return 0
    #if ra[-1] >= min_range[-1]:
    return len(min_range)
    #else:
    #    return len(ra)



def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
