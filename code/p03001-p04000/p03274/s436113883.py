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

N, K = getMN()
candles = getlist()

shift = N - K + 1
ans = 400000000
for i in range(shift):
    l, r = candles[i] ,candles[i+K-1]
    if r > 0:
        if l >= 0:
            cost = r
        else:
            cost = min(r + 2*abs(l), 2*r + abs(l))
    elif r == 0:
        cost = abs(l)
    else:
        cost = abs(l)
    if cost < ans:
        ans = cost


print(ans)

