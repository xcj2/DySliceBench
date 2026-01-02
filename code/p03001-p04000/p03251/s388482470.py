import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


N, M, X, Y = map(int, input().split())
x = readints()
y = readints()
# print(x)
# print(y)


def func(z):
    if (X < z and z <= Y):
        pass
    else:
        return False
    for i in range(N):
        if x[i] < z:
            pass
        else:
            return False
    for i in range(M):
        if y[i] >= z:
            pass
        else:
            return False
    return True


for i in range(-10000, 10000):
    if func(i) == True:
        print('No War')
        exit()
print('War')
