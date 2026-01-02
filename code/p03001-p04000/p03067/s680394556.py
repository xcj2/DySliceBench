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
    a, b, c = makeMultiInteger(input_string[0])
    #print(a, b, c)
    if a >= c and b <= c:
        return "Yes"
    if b >= c and a <= c:
        return "Yes"
    return "No"


def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
