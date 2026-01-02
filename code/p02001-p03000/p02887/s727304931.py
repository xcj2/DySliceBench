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
ct = 1
n = ip()
a = input()
current = a[0]
for i in range(1,n):
    if current != a[i]:
        current = a[i]
        ct+=1
print(ct)
