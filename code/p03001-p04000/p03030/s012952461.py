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
    N = makeMultiInteger(input_string[0])
    S = makeStringMatrix(input_string[1:])
    for _i, s in enumerate(S):
        s.append(_i+1)
    S = sorted(S, key=lambda x: x[0])
    a = []
    i = 0
    for _i, s in enumerate(S):
        #print(s)
        if a != []:
            if s[0] == a[i-1][0]:
                a.append(s)
            else:
                if len(a) > 1:
                    a = sorted(a, key=lambda x: int(x[1]), reverse=True)
                    #print(a)
                    for _a in a:
                        print(_a[2])
                else:
                    for _a in a:
                        print(_a[2])
                i = 0
                a = []
                a.append(s)
        else:
            a.append(s)
    if a != []:
        if len(a) > 1:
            a = sorted(a, key=lambda x: int(x[1]), reverse=True)
            for _a in a:
                print(_a[2])
        else:
            for _a in a:
                print(_a[2])


def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    #print(answer)


if __name__ == '__main__':
    main()
