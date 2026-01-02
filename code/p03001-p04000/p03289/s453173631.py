from statistics import mean, median,variance,stdev
import sys
import math
import fractions

def j(q):
    if q==1: print("AC")
    else:print("WA")
    exit(0)


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())

#n = ip()                              #入力整数1つ
#n,k= (int(i) for i in input().split())      #入力整数横2つ
#x,y,z = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列

#jの変数はしようできないので注意
#xor は(a ^ b)でいける

if a[0] != 'A':j(0)
b = a[2:len(a)-1]
if b.count('C') != 1:j(0)
if a[len(a)-1] == 'C':j(0)
b = a[1:]
for i in range(1,len(a)):
    p = a[i].lower()
    if not (p == a[i] or a[i]=='C'):
        j(0)
j(1)