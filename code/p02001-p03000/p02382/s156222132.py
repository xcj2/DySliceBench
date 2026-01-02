import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

def p1(x, y, n):
    D = []
    for i in range(n):
        D.append(abs(x[i] - y[i]))
    return sum(D)

def p2(x, y, n):
    D = []
    for i in range(n):
        D.append(abs(x[i] - y[i]))
        D[i] *= D[i]
    Sum = sum(D)
    return math.sqrt(Sum)

def p3(x, y, n):
    D = []
    for i in range(n):
        D.append(abs(x[i] - y[i]))
        D[i] = D[i] * D[i] * D[i]
    Sum = sum(D)
    return math.pow(Sum, 1 / 3)

def pX(x, y, n):
    D = []
    for i in range(n):
        D.append(abs(x[i] - y[i]))
    return max(D)

print('{:6f}'.format(p1(x, y, n)))
print('{:6f}'.format(p2(x, y, n)))
print('{:6f}'.format(p3(x, y, n)))
print('{:6f}'.format(pX(x, y, n)))

