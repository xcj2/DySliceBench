S = input().split(" ")
N = int(S[0])
M = int(S[1])


def C(m, n):
    t = m
    s1 = 1
    while t > (m - n):
        s1 = s1 * t
        t = t - 1

    s2 = 1

    t = n
    while t >= 1:
        s2 = s2 * t
        t = t - 1

    return int(s1 / s2)


def A(m, n):
    s = 1
    t = m

    while t > m - n:
        s = (s * t) % 1000000007
        t = t - 1

    return s


def calculate(maxValue, minValue):
    if maxValue > minValue + 1:
        return 0

    if maxValue == minValue:
        S = A(maxValue,maxValue)
        return  2 * S * S

    return A(maxValue,maxValue) * A(minValue,minValue)

result = calculate(max(N,M),min(N,M))

print(result % 1000000007)