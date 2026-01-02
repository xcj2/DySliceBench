from statistics import mean, median,variance,stdev
import sys
import math
import fractions

def j(q):
    if q==1: print("Yes")
    else:print("No")
    exit(0)


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())

#x = ip()                              #入力整数1つ
#x,y= (int(i) for i in input().split())      #入力整数横2つ
#x,y,z = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
s = input()                                  #入力文字列
#a = input().split()                          #入力文字配列

#jの変数はしようできないので注意

t = input()
l = len(t)
a=t
for i in range(l):
    b = [a[l-1],a[:l-1]]
    a = ''.join(b)
    if a==s:
        j(1)
j(0)