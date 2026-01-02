import numpy as np
import bisect
from collections import deque

X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

YZ = Y * Z

def createBitArray(X, Y, Z):
    size = X*Y*Z // 60 + 1
    return(np.zeros(size, 'int64'))

def getBit(R, a, b, c):
    pos = a * YZ + b * Z + c
    loc = pos // 60
    bit = 2 ** (pos % 60)
    return(R[loc] & bit)

def putBit(R, a, b, c):
    pos = a * YZ + b * Z + c
    loc = pos // 60
    bit = 2 ** (pos % 60)
    R[loc] = R[loc] | bit

R = createBitArray(X, Y, Z)

l = []
m = []

M = A[0] + B[0] + C[0]
position = bisect.bisect(l, M)
bisect.insort(l, M)
m.insert(position, (0, 0, 0))
putBit(R, 0, 0, 0)

for i in range(K):
    print(l[len(m)-1])

    a, b, c = m[len(m)-1]

    del l[len(m)-1]
    del m[len(m)-1]

    if a+1 < X and getBit(R, a+1, b, c) == 0:
        M = A[a+1] + B[b] + C[c]
        position = bisect.bisect(l, M)
        bisect.insort(l, M)
        m.insert(position, (a+1, b, c))
        putBit(R, a+1, b, c)

    if b+1 < Y and getBit(R, a, b+1, c) == 0:
        M = A[a] + B[b+1] + C[c]
        position = bisect.bisect(l, M)
        bisect.insort(l, M)
        m.insert(position, (a, b+1, c))
        putBit(R, a, b+1, c)

    if c+1 < Z and getBit(R, a, b, c+1) == 0:
        M = A[a] + B[b] + C[c+1]
        position = bisect.bisect(l, M)
        bisect.insort(l, M)
        m.insert(position, (a, b, c+1))
        putBit(R, a, b, c+1)
