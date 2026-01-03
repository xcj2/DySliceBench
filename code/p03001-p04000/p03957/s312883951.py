from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy
#以下てんぷら
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
def printrow(a):
    for i in range(len(a)):
        print(a[i])
def combinations(n,r):
    if n<r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations(n,r):
    if n<r:return 0
    return math.factorial(n) // math.factorial(n - r)
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


#n = ip()                                     #入力整数1つ
#a,b,c,k= (int(i) for i in input().split())       #入力整数横2つ以上
#a = [int(i) for i in input().split()]        #入力整数配列
a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しに4 3sum変数使用はsum関数使用できないので注意
step = 0
for i in range(len(a)):
    if step:
        if a[i] == 'F':j(1)
    else:
        if a[i] == 'C':step+=1
j(0)