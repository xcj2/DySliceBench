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
import sys
from array import array
from collections import deque

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
def hcfnaive(a,b):#最大公約数 math.gcdが使えない時の手段として入れとく。pythonが更新されたらいらなくなるはず
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)


N = intinput()
dic = {}
ans = 0
true_person = 0
flag_contradiction = 0
for i in range(N):
    dic[i] = {}

for i in range(N):
    A = intinput()
    for j in range(A):
        x,y = splitintinput()
        dic[i][x-1] = y

for i in range(2**N):
    tmp = format(i, 'b').zfill(N)
    true_person = tmp.count('1')
    flag_contradiction = 0
    for j in range(N):
        if int(tmp[j]) == 1:
            for k in dic[j]:
                if dic[j][k] != int(tmp[k]):
                    flag_contradiction = 1
                    break
    if flag_contradiction == 0:
        ans = max(ans,true_person)

print(ans)

