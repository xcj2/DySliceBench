import math


def eratos(num):
    isPrime = [True] * (num + 1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.sqrt(num))):
        for j in range(2 * i, num, i):
            isPrime[j] = False
    return isPrime


def isLike(isPrime):
    n = len(isPrime)
    array = [False] * (n - 1)
    for i in range(n - 1):
        if isPrime[i] and isPrime[(i + 1) // 2]:
            array[i] = True
    return array


def cumSum(array):
    n = len(array)
    cum = [0] * (len(array))
    for i in range(1, n):
        cum[i] = cum[i - 1]
        cum[i] += 1 if array[i] else 0

    return cum


def solve(l, r, cum):
    return cum[r] - cum[l - 1]


Q = int(input())

isPrime = eratos(10 ** 5 + 1)
array = isLike(isPrime)
cum = cumSum(array)

for i in range(Q):
    l, r = map(int, input().split())
    print(solve(l, r, cum))
