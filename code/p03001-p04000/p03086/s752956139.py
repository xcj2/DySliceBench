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
    S = input_string
    cnt = 0
    maxCnt = 0
    for N in S:
        if N == 'A':
            cnt += 1
        elif N == 'T':
            cnt += 1
        elif N == 'G':
            cnt += 1
        elif N == 'C':
            cnt += 1
        else:
            if cnt > maxCnt:
                maxCnt = cnt
            cnt = 0
        if cnt > maxCnt:
            maxCnt = cnt
    return maxCnt


def main():
    input_lines = stdin.readline()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
