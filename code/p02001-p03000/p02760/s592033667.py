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
def hcfnaive(a,b):#最大公約数 math.gcdが使えない時の手段として入れとく。pythonが更新されたらいらなくなるはず
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

card = [[0] * 3 for i in range(3)]
bingo = [[0] * 3 for i in range(3)]
flag = 0
for i in range(3):
    card[i][0],  card[i][1], card[i][2] = splitintinput()

N = intinput()
for i in range(N):
    b = intinput()
    for j in range(3):
        for k in range(3):
            if card[j][k] == b:
                bingo[j][k] = 1

for i in range(3):
    for j in range(3):
        if bingo[i][j] == 0:
            break
    else:
        flag = 1

for i in range(3):
    for j in range(3):
        if bingo[j][i] == 0:
            break
    else:
        flag = 1

for i in range(3):
    if bingo[i][i] == 0:
        break
else:
    flag = 1

for i in range(3):
    if bingo[i][2-i] == 0:
        break
else:
    flag = 1

if flag == 0:
    print('No')
else:
    print('Yes')