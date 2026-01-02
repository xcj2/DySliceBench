import math
import fractions
import copy
import numpy as np
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
def iprow():
    return [int(i) for i in input().split()]
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

#n = ip()                                     #入力整数1つ
x,y= (int(i) for i in input().split())       #入力整数横2つ以上
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(m)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#a.pop(0)は10^5あるときTLEしやすい!注意!抜くなら逆ソート!

a = iprow()

dp = [0]
for i in range(1,x+1):
    dp.append(dp[i-1]+a[i-1])
s = 0
while dp[s] <= y and s<=x-1 :s+=1
if s == x and dp[s]<=y :s+=1
print(s)