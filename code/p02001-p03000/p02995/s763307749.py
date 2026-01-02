import math
import copy
import fractions
import numpy as np

# ===FUNCTION===

def getInputNum():
    inputNum = int(input())
    return inputNum

def getInputListInt():
    outputoData = []
    inputData = input().split()
    outputData = [int(n) for n in inputData]

    return outputData

def getSomeInputInt(n):
    outputDataList = []
    for i in range(n):
        inputData = int(input())
        outputDataList.append(inputData)

    return outputDataList

def getSomeInputListInt(n):
    inputDataList = []
    outputDataList = []
    for i in range(n):
        inputData = input().split()
        inputDataList = [int(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList

# ===CODE===

def GCD(x, y):
    return x if y == 0 else GCD(y, x % y)


def LCM(x, y):
    return x // GCD(x, y) * y

num = getInputListInt()

a = num[0]
b = num[1]
c = num[2]
d = num[3]

c_modzero = b//c - (a-1)//c
d_modzero = b//d - (a-1)//d

cd = LCM(c, d)

cd_modzero = b//cd - (a-1)//cd

ans = b - a + 1 - (c_modzero + d_modzero - cd_modzero)

print(int(ans))

