from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy
from operator import itemgetter
#以下てんぷら
def j(q):
    if q==1: print("YES")
    else:print("NO")
    exit(0)


def ct(x,y):
    if (x>y):print("+")
    elif (x<y): print("-")
    else: print("?")

def ip():
    return int(input())
n = ip()                                     #入力整数1つ
#a,b,c= (int(i) for i in input().split())       #入力整数横2つ以上
a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)

#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#こっから本文
dp = [-1 for i in range(n+1)]
dp[0] = 0
dp[1] = 0
dp[2] = abs(a[0]-a[1])
#dp[3]  =     min(dp[2] +  abs(a[2] - a[1]) ,     dp[1] +   abs(a[2] - a[0]))

for i in range(3,n+1):
    dp[i] = min(dp[i-1] + abs(a[i-1] - a[i-2]) , dp[i-2] + abs(a[i-1]-a[i-3]) )
 #   print(dp)
print(dp[n])