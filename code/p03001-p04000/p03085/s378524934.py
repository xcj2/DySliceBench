from sys import stdin
import math
import itertools


def makeIntMatrix(lines):
    intMatrix = []
    for a in makeStringMatrix(lines):
        intMatrix += [int(b) for b in a]
    return intMatrix


def makeStringMatrix(lines):
    stringMatrix = [line.split() for line in lines]
    return stringMatrix


def makeInt(line):
    return int(line.rstrip())


def makeMultiInteger(line):
    return [int(x) for x in line.rstrip().split()]


def solve(input_string):
    N = input_string
    if N == 'A':
        return 'T'
    elif N == 'T':
        return 'A'
    elif N == 'G':
        return 'C'
    elif N == 'C':
        return 'G'


def main():
    input_lines = stdin.readline().rstrip()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
