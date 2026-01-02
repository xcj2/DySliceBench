import math
import fractions
import copy
import numpy as np
def j(q):
    if q==1: print("Yes")
    elif q == 0:print("No")
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
def ips():
    return (int(i) for i in input().split())
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

#n,m = ips()
a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(m)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#a.pop(0)は10^5あるときTLEしやすい!注意!抜くなら逆ソート!
s = []
for i in range(4):
    s.append(a[i])
s.sort()
if s[0] == s[1] and s[2] == s[3] and s[1] != s[2]:j(1)
j(0)
