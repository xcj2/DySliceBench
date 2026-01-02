import copy

def j(n):
    if n:print("yes")
    else:print("no")
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
n = ip()
a = iprow()
cons = 0
m = 0
for i in range(n-1):
    if a[i] >= a[i+1]:
        cons+=1
    else:
        m = max(m,cons)
        cons = 0
print(max(m,cons))