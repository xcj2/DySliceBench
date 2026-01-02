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
    l = [0, a, b, c, d, e]
    m = 9
    m_i = 1
    for i in range(len(l)):
        if m > l[i] % 10 and l[i] % 10 > 0:
            m = l[i] % 10
            m_i = i
    if m != 0:
        temp = l[-1]
        l[-1] = l[m_i]
        l[m_i] = temp

    #ls = sorted(l)
    #print(ls)
    lst = 0
    alst = 0
    i = 1
    # 10ずつ足されるのがベスト
    at = 0
    while(i < 6):
        if at >= l[i-1]:
            #print(at, ls[i-1])
            if i != 5:
                #print(at)
                alst += at
                #print(ls[i])
            else:
                #print(at)
                alst += at
                alst += l[i]
                return alst
            at = 0
            i += 1
            #print(alst)
        else:
            at += 10


def main():
    answer = solve()
    print(answer)


if __name__ == '__main__':
    main()
