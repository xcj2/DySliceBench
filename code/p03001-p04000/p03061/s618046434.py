import sys
sys.setrecursionlimit(10**6)

def Lgcd(i):
    if i == 0:
        return 0
    if i == 1:
        return a_s[0]
    if i in Lmemo:
        return Lmemo[i]
    re = gcd(Lgcd(i - 1), a_s[i - 1])
    Lmemo[i] = re
    return re


def Rgcd(i):
    if i == n - 1:
        return 0
    if i == n - 2:
        return a_s[-1]
    if i in Rmemo:
        return Rmemo[i]
    re = gcd(Rgcd(i + 1), a_s[i + 1])
    Rmemo[i] = re
    return re


def gcd(a, b):
    if a * b == 0:
        return a + b
    while 1:
        a, b = b, a % b
        if b == 0:
            return a


Lmemo = {}
Rmemo = {}
n = int(input())
a_s = list(map(int, input().split()))
mx = 0
for i in range(n):
    g = gcd(Lgcd(i),Rgcd(i))
    if g > mx:
        mx = g
print(mx)
