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
    r, g, b, n = makeMultiInteger(input_string[0])
    c = 0
    nr = int(n/r)+1
    ng = int(n/g)+1
    nb = int(n/b)+1
    #print(r, g, b, n, nr, ng, nb)
    # 二分探索？
    """
    for i in range(nr):
        _sum = i*r
        if _sum == n:
            c += 1
            break
        for j in range(ng):
            _sum = j*g+i*r
            if _sum == n:
                c += 1
                break
            for k in range(nb):
                _sum = i*r + j*g + k*b
                #print(_sum)
                if _sum == n:
                    c += 1
                    break
    """
    for i in range(nr):
        _sum = i*r
        if _sum > n:
            break
        for j in range(ng):
            _sum = j*g+i*r
            if _sum > n:
                break
            rg_sum = j*g+i*r
            if (n - rg_sum) % b == 0:
                c += 1
            """
            for k in range(nb):
                _sum = i*r + j*g + k*b
                #print(_sum)
                if _sum == n:
                    c += 1
                    break
            """
    return c


def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
