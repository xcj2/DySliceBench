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
    s = list(input_string[0][:])
    c_1 = 0
    for i in range(len(s))[1:]:
        if s[i] == s[i-1]:
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i] = "1"
            c_1 += 1
    c_2 = 0
    for i in range(len(s))[::-1][1:]:
        if s[i] == s[i+1]:
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i] = "1"
            c_2 += 1
    return c_2 if c_2 > c_1 else c_1



def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
