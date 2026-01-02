def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

burger = [1] + [0 for i in range(50)]
niku = [1] + [0 for i in range(50)]
for i in range(50):
    burger[i+1] = 2 * burger[i] + 3
    niku[i+1] = 2 * niku[i] + 1

n, x = getMN()

def singleburger(x):
    if x <= 1:
        return 0
    elif x <= 4:
        return x-1
    else: return 3

def intonburger(n,x):
    if n == 1:
        return singleburger(x)
    if x <= 1:
        return 0
    elif x <= burger[n-1] + 1:
        return intonburger(n-1, x-1)
    elif x == burger[n-1] + 2:
        return niku[n-1] + 1
    elif x <= 2 * burger[n-1] + 2:
        return niku[n-1] + 1 + intonburger(n-1, x-burger[n-1]-2)
    else:
        return 2 * niku[n-1] + 1

print(intonburger(n,x))

