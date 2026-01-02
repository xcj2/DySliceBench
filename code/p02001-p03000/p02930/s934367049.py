import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


import math

n = getN()

def judge(i, j):
    if i == j:
        print("ERROR", i)
        sys.exit()
    res = 1
    while(True):
        if i % 2 != j % 2:
            return res
        else:
            res += 1
            i = i>>1
            j = j>>1


for i in range(1, n+1):
    level = []
    for j in range(i+1, n+1):
        level.append(judge(i, j))

    print(*level)