n = int(input())
*arr, = map(int, input().split())

def pairwise_coprime(arr):
    mx = max(arr)
    data = [0] * (mx + 1)
    for v in arr:
        data[v] += 1
        if v > 1 and data[v] > 1:
            return False
    primes = [1] * (mx + 1)
    for v in range(2, mx + 1):
        if primes[v]:
            cnt = 0
            if data[v]:
                cnt += 1
            for nonprime in range(2 * v, mx + 1, v):
                primes[nonprime] = 0
                if data[nonprime]:
                    cnt += 1
            if cnt > 1:
                return False
    return True

def gcd(a, b):
    if a > b:
        a, b = b, a

    while a:
        # gcd(a, b) = gcd(b, a % b)
        b, a = a, b % a
    return b


def setwise_coprime(arr):
    common_gcd = arr[0]
    for i in range(1, len(arr)):
        common_gcd = gcd(common_gcd, arr[i])
    return common_gcd == 1


if pairwise_coprime(arr):
    print("pairwise coprime")
elif setwise_coprime(arr):
    print("setwise coprime")
else:
    print("not coprime")
