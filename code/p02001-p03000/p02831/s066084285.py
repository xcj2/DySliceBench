# from fractions import gcd
# mod = 10 ** 9 + 7
# N = int(input())
# a = list(map(int,input().split()))
# a,b,c = map(int,input().split())
# ans = [0] * N
# math.ceilで切り上げ
# dp = [[0] * 4 for i in range(3)] #2次元配列初期化
# dp = [[[0] * 2 for i in range(3)] for j in range(5)]
# (ord('A'))でASCII出力 Aは65
import math
import statistics
import string


def intinput():
    return int(input())
def listintinput():
    return list(map(int, input().split()))
def splitintinput():
    return map(int, input().split())
def factorialsurplus(x, y, z):  # xからyまでの階乗をzで割ったあまりを求める
    ret = 1
    for i in range(x, y + 1):
        ret = (ret * i) % z
    return (ret)
def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    sq = int(math.sqrt(x))
    for i in range(2,sq+1):
        if x % i == 0:
            return False
    return True
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

a,b = splitintinput()
g = hcfnaive(a,b)
print(int(a*b/g))