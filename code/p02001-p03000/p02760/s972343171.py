A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = A1 + A2 + A3

N = int(input())

# 印をつける
for i in range(N):
    b = int(input())
    
    for index in range(len(A)):
        a = A[index]
        if a == b:
            A[index] = 0     # 0を印とする

def isExistTatePair():
    for i in range(3):
        sum = 0
        for j in range(3):
            sum += A[3 * j + i]
        if sum == 0:
            return True
    return False

def isExistYokoPair():
    for i in range(3):
        sum = 0
        for j in range(3):
            sum += A[3 * i + j]
        if sum == 0:
            return True
    return False

def isExistNanamePair():
    sum = 0
    for i in range(3):
        sum += A[3 * i + i]
    if sum == 0:
        return True
    
    sum = 0
    for i in range(3):
        sum += A[3 * (i + 1) - (i + 1)]
    if sum == 0:
        return True
    return False

isExistPair = isExistTatePair() or isExistYokoPair() or isExistNanamePair()
print('Yes' if isExistPair else 'No')