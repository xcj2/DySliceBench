import collections
import math
import re
import numpy
def ai():return input()#s
def a():return int(input())#a,n or k
def ma():return map(int, input().split())#a,b,c,d or n,k
def ms():return map(str, input().split())#,a,b,c,d
def lma():return list(map(int, input().split()))#x or y
def lms():return list(map(str, input().split()))#x or y
def say(i):return print("Yes" if i == 0 else "No")
def Say(i):return print("YES" if i == 0 else "NO")
k= [0]
l = []
f = 0
s=0
c=0
e =1
a  =a()
x = lma() +[0]
m = min(x)
for i in range(1,a+1):
    if x[i] < x[i-1]:
        s+=x[i-1]-m
        m = x[i]
print(s)