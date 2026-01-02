
N,X=[int(_) for _ in input().split()]
def countP(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        return 1 + countP(n-1) * 2

def countBP(n):
    if n == 0:
        return 3
    elif n == 1:
        return 5
    else:
        return 3 + countBP(n-1) * 2

def countPinBP(n,x):
    if x == 1:
        return 0
    if n == 0:
        if x == 1:
            return 0
        else:
            return 1
    elif n == 1:
        if x == 1:
            return 0
        elif x < 5:
            return x - 1
        else:
            return 3
    else:
        #iH = countBP(n) // 2
        iH = 1 + countBP(n-1)
        if x <= iH:
            return countPinBP(n-1,x-1)
        elif x == iH + 1:
            return countP(n-1) + 1
        else:
            return countP(n-1) + 1 + countPinBP(n - 1, x - iH - 1)
print(countPinBP(N,X))
