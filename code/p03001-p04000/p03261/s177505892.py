from statistics import mean, median,variance,stdev
import sys
import math
import fractions
def j(a):
    if a: print("Yes")
    else :print("No")


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())

x = ip()                              #入力整数1つ
#x,y = (int(i) for i in input().split())      #入力整数横2つ
#x,y,z = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列

a = []
a.append(input())
s = 1
for i in range(1,x):
    l = input()
    if l in a: s =0
    a.append(l)
    if l[0] != a[i-1][len(a[i-1])-1]: s=0
j(s)