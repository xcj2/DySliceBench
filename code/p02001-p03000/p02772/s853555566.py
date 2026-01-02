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
import string

def intinput():
    return int(input())

def listintinput():
    return list(map(int,input().split()))

def splitintinput():
    return map(int,input().split())

N = intinput()
A = listintinput()
flag = 0
for i in A:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            flag = 1

if flag == 0:
    print('APPROVED')
else:
    print('DENIED')
