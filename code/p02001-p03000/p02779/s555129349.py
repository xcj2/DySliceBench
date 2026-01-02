#from fractions import gcd
#mod = 10 ** 9 + 7
#N = int(input())
#a = list(map(int,input().split()))
#a,b,c = map(int,input().split())
#ans = [0] * N
#math.ceilで切り上げ
import math
import string

def intinput():
    return int(input())

def listintinput():
    return list(map(int,input().split()))

def splitintinput():
    return map(int,input().split())

N = intinput()
dic = {}
A = listintinput()
flag = 0
for i in A:
    if i in dic:
        flag = 1
        break
    else:
        dic[i] = 1

if flag == 0:
    print('YES')
else:
    print('NO')
