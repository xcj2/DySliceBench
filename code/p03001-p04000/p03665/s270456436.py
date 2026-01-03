def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


N, P = readmap()
A = readlist()

for i in range(N):
    A[i] = A[i] % 2

cnt_0 = A.count(0)
cnt_1 = A.count(1)


def fact(n):
    if n == 0:
        return 1
    elif n > 0:
        return n*fact(n-1)


def nCr(n,r):
    return fact(n)/(fact(r)*fact(n-r))


if P == 0:
    ans = 2 ** cnt_0
    num = 0
    for i in range(cnt_1 // 2 + 1):
        num += nCr(cnt_1, 2*i)
    ans *= num
    print(int(ans))
else:
    ans = 2 ** cnt_0
    num = 0
    for i in range((cnt_1 - 1) // 2 + 1):
        num += nCr(cnt_1, 2 * i + 1)
    ans *= num
    print(int(ans))
