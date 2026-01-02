import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


import math
MOD = 10**9 + 7

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
        ans %= MOD

    return ans % MOD

n = getN()
s = input().strip()

ans = 1

open = 0
for c in s:
    # print(c, ans, open, cur)
    if c == "B":
        if open%2 == 0:
            open += 1

        else:
            if open == 0:
                print(0)
                sys.exit()
            ans *= open
            ans %= MOD
            open -= 1


    else:
        if open%2 == 1:
            open += 1

        else:
            if open == 0:
                print(0)
                sys.exit()
            ans *= open
            ans %= MOD
            open -= 1


if open != 0:
    print(0)
    sys.exit()
print((ans * factorial(n)) % MOD)