def solve(N, strX):
    def getNum1s(numD):
        num1s = [0] * (1<<numD)
        for S in range(1, 1<<numD):
            num1s[S] = num1s[S ^ (S & -S)] + 1
        return num1s
    num1s = getNum1s(20)

    fs = [0] * (N+1)
    for x in range(1, N+1):
        fs[x] = fs[x%num1s[x]] + 1

    M = strX.count('1')
    M1, M9 = M+1, M-1

    XmodM1 = 0
    for X in strX:
        XmodM1 *= 2
        XmodM1 += int(X)
        XmodM1 %= M1
    XmodM9 = 0
    for X in strX:
        XmodM9 *= 2
        XmodM9 += int(X)
        XmodM9 %= M9

    modM1s = []
    modM1 = 1
    for d in range(N+2):
        modM1s.append(modM1)
        modM1 *= 2
        modM1 %= M1

    modM9s = []
    modM9 = 1
    for d in range(N+2):
        modM9s.append(modM9)
        modM9 *= 2
        modM9 %= M9

    anss = []
    for X, modM1, modM9 in zip(strX[::-1], modM1s, modM9s):
        if X == '0':
            Y2 = (XmodM1 + modM1) % M1
        else:
            Y2 = (XmodM9 - modM9) % M9
        ans = fs[Y2] + 1
        anss.append(ans)

    return anss[::-1]


def solve2(N, strX):
    def getNum1s(numD):
        num1s = [0] * (1<<numD)
        for S in range(1, 1<<numD):
            num1s[S] = num1s[S ^ (S & -S)] + 1
        return num1s
    num1s = getNum1s(20)

    fs = [0] * (N+1)
    for x in range(1, N+1):
        fs[x] = fs[x%num1s[x]] + 1

    M = strX.count('1')
    M1, M9 = M+1, M-1

    XmodM1 = 0
    for X in strX:
        XmodM1 *= 2
        XmodM1 += int(X)
        XmodM1 %= M1

    modM1s = []
    modM1 = 1
    for d in range(N+2):
        modM1s.append(modM1)
        modM1 *= 2
        modM1 %= M1

    anss = []
    for X, modM1 in zip(strX[::-1], modM1s):
        if X == '0':
            Y2 = (XmodM1 + modM1) % M1
            ans = fs[Y2] + 1
        else:
            ans = 0
        anss.append(ans)

    return anss[::-1]


N = int(input())
strX = input().rstrip()

num1 = strX.count('1')

if num1 == 0:
    anss = [1] * N
elif num1 == 1:
    anss = solve2(N, strX)
else:
    anss = solve(N, strX)

print('\n'.join(map(str, anss)))
