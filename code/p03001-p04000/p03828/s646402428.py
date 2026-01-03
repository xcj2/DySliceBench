from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy

def j(q):
    if q==1: print("YES")
    else:print("NO")
    exit(0)


def ct(x,y):
    if (x>y):print("GREATER")
    elif (x<y): print("LESS")
    else: print("EQUAL")

def ip():
    return int(input())


def calculate(a):
    s = 0
    for i in range(len(a)):
        for k in range(i+1,len(a)):
            s+=(a[i]*a[k])
    return s

n = ip()                              #入力整数1つ
#n,m= (int(i) for i in input().split())      #入力整数横2つ
#n,a,b = (int(i) for i in input().split())    #入力整数横3つ
#n,a,b,c= (int(i) for i in input().split())  #入力整数横4つ
#s = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(h)]
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
if n == 1:
    print(1)
elif n==2:
    print(2)
else:
    l = [0]* ( n + 1 )

    for i in range(n+1):
        s = []
        value = i
        search = 1
        while value != 1 and search <= math.sqrt(value):
            search+=1
            if value%search == 0:
                s.append(search)
                value = value//search
                search = 1
        if search > math.sqrt(value) and value > 1:
            s.append(value)

        for p in range(len(s)):
            l[s[p]]+=1
    ans = 1
    for i in range(2,n+1):
        if l[i]:ans*=(l[i]+1)
    print(ans%(pow(10,9)+7))