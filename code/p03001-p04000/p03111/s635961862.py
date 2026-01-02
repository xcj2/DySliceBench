import math
N, A, B, C = 5, 100, 90, 80
ARR = [
    98,
    40,
    30,
    21,
    80
]

# N,A,B,C = 8, 100, 90, 80
# ARR = [
#     100,
#     100,
#     90,
#     90,
#     90,
#     80,
#     80,
#     80,
# ]


# N,A,B,C,= 8, 1000, 800, 100
# ARR = [
#     300,
#     333,
#     400,
#     444,
#     500,
#     555,
#     600,
#     666,
# ]

N,A,B,C = map(int,input().split())
ARR = []
for i in range(N):
    ARR.append(int(input()))

def calculate(n, arr, a, b, c):
    result = []
    for i in range(4 ** n):
        materialA = set()
        materialB = set()
        materialC = set()
        materialNone = set()
        for j in range(n):
            s = (i >> 2 * j & 1)
            t = (i >> (2 * j + 1) & 1)
            if (s == 0) and (t == 0):
                materialA.add(j)
            if (s == 1) and (t == 0):
                materialB.add(j)
            if (s == 0) and (t == 1):
                materialC.add(j)
            if (s == 1) and (t == 1):
                materialNone.add(j)

        ok, mp = judge(n, arr, a, b, c, materialA, materialB, materialC, materialNone)
        if ok:
            result.append(mp)
    print(int(min(result)))

def judge(n, arr, a, b, c, materialA, materialB, materialC, materialNone):


    if materialNone == n:
        return False, -1

    if len(materialA & materialB) > 0:
        return False, -1

    if len(materialA & materialC) > 0:
        return False, -1

    if len(materialB & materialC) > 0:
        return False, -1

    if len(materialA) == 0:
        return False, -1

    if len(materialB) == 0:
        return False, -1

    if len(materialC) == 0:
        return False, -1

    mpA = 0
    a = a - calculateResult(arr,materialA)
    mpA += math.fabs(a)
    if len(materialA) > 1:
        mpA += 10 * (len(materialA) - 1)

    mpB = 0
    b = b - calculateResult(arr,materialB)
    mpB += math.fabs(b)
    if len(materialB) > 1:
        mpB += 10 * (len(materialB) - 1)

    mpC = 0
    c = c - calculateResult(arr,materialC)
    mpC += math.fabs(c)
    if len(materialC) > 1:
        mpC += 10 * (len(materialC) - 1)


    return True,mpA+mpB+mpC

def calculateResult(arr,material):
    result = 0
    for m in material:
        result = result + arr[m]
    return result

calculate(N, ARR, A, B, C)
