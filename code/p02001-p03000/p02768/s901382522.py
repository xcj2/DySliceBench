#from fractions import gcd
#mod = 10 ** 9 + 7
#N = int(input())
#a = list(map(int,input().split()))
#a,b,c = map(int,input().split())
#ans = [0] * N
#math.ceilで切り上げ
#dp = [[0] * 4 for i in range(3)] #2次元配列初期化
#dp = [[[0] * 2 for i in range(3)] for j in range(5)]
#(ord('A'))でASCII出力 Aは65
import math
import statistics
import string

def intinput():
    return int(input())

def listintinput():
    return list(map(int,input().split()))

def splitintinput():
    return map(int,input().split())

def repeatsurplus(x,y,z): #xのy乗をzで割ったあまりを高速に求める
    ret = 1
    m = y
    tmp = x
    for i in range(100000):
        if m == 1:
            ret = (ret * tmp) % z
            break
        if m % 2 == 1:
            ret = (ret * tmp) % z
        m = m // 2
        tmp = (tmp * tmp) % z
    return(ret)

def factorialsurplus(x,y,z): #xからyまでの階乗をzで割ったあまりを求める
    ret = 1
    for i in range(x, y+1):
        ret = (ret * i) % z
    return(ret)
    
    
    
n,a,b = splitintinput()
de = 10 ** 9 + 7
ans = repeatsurplus(2,n,de) - 1
ansa = factorialsurplus(n-a+1, n, de) * repeatsurplus(factorialsurplus(1, a, de), de-2, de)
ansb = factorialsurplus(n-b+1, n, de) * repeatsurplus(factorialsurplus(1, b, de), de-2, de)
print((ans-ansa-ansb+2*de)%de)

