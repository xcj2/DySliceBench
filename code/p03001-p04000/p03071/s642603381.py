from sys import stdin
import math
import itertools
import copy


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
    a = makeMultiInteger(input_string[0])
    _max = 0
    two = copy.deepcopy(a)
    c = two[0]
    two[0] -= 1
    c += two[0]
    two[0] -= 1
    if _max < c:
        _max = c

    two = copy.deepcopy(a)
    c = 0
    c = two[0]
    two[0] -= 1
    c += two[1]
    two[1] -= 1
    if _max < c:
        _max = c

    two = copy.deepcopy(a)
    c = 0
    c = two[1]
    two[1] -= 1
    c += two[1]
    two[1] -= 1
    if _max < c:
        _max = c
    return _max


def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
