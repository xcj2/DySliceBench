import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def judgement(n, pos):
    return (int(pos) - 1) * math.factorial(n - 1)

def position(target, list):
    pos = 0
    for i in list:
        if (int(target) > int(i)):
            pos += 1
    return pos + 1

def calculateRank(list):
    targetNum = 0
    rank = 0
    for i in range(N - 1):
        targetNum = list[0]
        list.pop(0)
        targetPosition = position(targetNum, list)
        rank += judgement(N - i, targetPosition)

    return rank

rankA = calculateRank(P)
rankB = calculateRank(Q)

print(abs(rankA - rankB))