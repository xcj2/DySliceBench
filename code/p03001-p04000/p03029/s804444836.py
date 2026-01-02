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
    a, p = makeMultiInteger(input_string[0])
    #print(a, p)
    p += a*3
    #print(p)
    return p//2


def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
