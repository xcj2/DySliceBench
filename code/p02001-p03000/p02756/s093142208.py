import copy

import math
import fractions

def j(n):
    if n:print("Yes")
    else:print("No")
    exit(0)
rem = 10 ** 9 + 7

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
def ipmultiplerow(n):
    a = []
    for i in range(n):
        a.append(ip())
    return a
def printrow(a):
    for i in a:
        print(i)

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

s = input()
n = ip()
addedleft = []
addedright = []
flip = 0
for i in range(n):
    cmd = input().split()
    #print(cmd)
    if len(cmd) == 1:
        flip+=1
        flip%=2
    else:
        if cmd[1] == "1":
            if flip == 0: addedleft.append(cmd[2])
            else: addedright.append(cmd[2])
        else: #cmd[2] == 2
            if flip == 0: addedright.append(cmd[2])
            else: addedleft.append(cmd[2])
#print("left", addedleft)
#print("right", addedright)
addedleft.reverse()
r = ''.join(addedright)
l = ''.join(addedleft)
ans  = ''.join([l,s,r])
if flip==0:
    print(ans)
else:
    for i in range(len(ans)):
        print(ans[-i-1],end='')