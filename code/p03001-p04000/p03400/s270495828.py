from statistics import mean, median,variance,stdev
import sys
import math
import fractions

def j(q):
    if q==1: print("YES")
    else:print("NO")
    exit(0)


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())

n = ip()                              #入力整数1つ
d,x= (int(i) for i in input().split())      #入力整数横2つ
#k,a,b = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列

#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
a =[]
for i in range(n):
    a.append(ip())
s = 0
for i in range(n):
    if d%a[i]:s+=d//a[i] + 1
    else: s+=(d//a[i])
print(s+x)