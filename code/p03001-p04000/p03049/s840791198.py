import math
import fractions
import copy
import numpy as np
#以下てんぷら
def j(q):
    if q==1: print("POSSIBLE")
    elif q == 0:print("IMPOSSIBLE")
    exit(0)
rem = pow(10,9)+7
"""
def ct(x,y):
    if (x>y):print("+")
    elif (x<y): print("-")
    else: print("?")
"""

def ip():
    return int(input())
def printrow(a):
    for i in a:
        print(i)
def combinations(n,r):
    if n<r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations(n,r):
    if n<r:return 0
    return math.factorial(n) // math.factorial(n - r)
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


n = ip()                                     #入力整数1つ
#n,m= (int(i) for i in input().split())       #入力整数横2つ以上
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(m)]    #入力セット(整数改行あり)(2/2)
a=[input() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#a.pop(0)は10^5あるときTLEしやすい!注意!抜くなら逆ソート!
#これを消すとなぜかWAになる呪い
type = [0 for i in range(4)]
s = 0
for i in a:
    s+=i.count("AB")
    if i[0] == 'B' and i[-1] == 'A': type[0]+=1    # B***A
    elif i[0] == 'B' and i[-1] != 'A': type[1]+=1  # B****
    elif i[0] != 'B' and i[-1] == 'A': type[2]+=1  # ****A
    elif i[0] != 'B' and i[-1] != 'A': type[3]+=1  # *****
if type[0] == 0:
    s+=min(type[1],type[2])
else:
    if type[1] or type[2]:
        s+=type[0]+ min(type[1],type[2])
    else:
        s+=type[0]-1
print(s)

