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


def solve():
    a = makeInt(input())
    b = makeInt(input())
    c = makeInt(input())
    d = makeInt(input())
    e = makeInt(input())
    l = [a, b, c, d, e]
    k = makeInt(input())
    flag = False
    for i in range(len(l)):
        for j in range(len(l)-1):
            if abs(l[i] - l[j+1]) > k:
                flag = True
    if flag:
        return ":("
    else:
        return "Yay!"


def main():
    answer = solve()
    print(answer)


if __name__ == '__main__':
    main()
