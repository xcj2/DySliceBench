#!usr/bin/env python3
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def LIR(n): return [LI() for i in range(n)]
mod = 1000000007

#A
"""
a,b,c = LI()
s = a+b+c
s /= 2
ans = (s*(s-a)*(s-b)*(s-c))**(1/2)
print(int(ans))
"""

#B
"""
s = int(input())
m = 1
lis = [True for i in range(1000001)]

while lis[s]:
    lis[s] = False
    if s % 2 == 1:
        s = 3*s+1
    else:
        s //= 2
    m += 1
print(m)
"""

#C
n = II()
h = LI()
ans = 0
while sum(h) != 0:
    l = 0
    while h[l] == 0: l += 1
    r = l
    while r < n:
        if h[r] == 0: break
        h[r] -= 1
        r += 1
    ans += 1
print(ans)
#D

#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T
