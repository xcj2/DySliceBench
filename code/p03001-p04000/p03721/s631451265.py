#!usr/bin/env python3
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def LIR(n): return [LI() for i in range(n)]

#A
"""
s = S()
if s[0] != "A":
    print("WA")
else:
    count = []
    for i in range(2,len(s)-1):
        if s[i] == "C": count.append(i)
    if len(count) != 1:
        print("WA")
    else:
        for i in range(1,len(s)):
            if i not in count:
                if s[i] == s[i].upper():
                    print("WA")
                    quit()
        print("AC")
"""

#B
"""
n,m,k = LI()
for i in range((n+1)//2):
    if (k - m*i) % (n - 2*i) == 0 and (k-m*i)//(n-2*i) >= 0 and (k-m*i)//(n-2*i) <= m:
        print("Yes")
        quit()
print("No")
"""

#C
from collections import defaultdict
n,k = LI()
d = defaultdict(int)
for i in range(n):
    a,b = LI()
    d[a] += b
s = list(d.items())
s.sort(key = lambda x:x[0])
su = 0
for i in range(len(s)):
    su += s[i][1]
    if su >= k:
        print(s[i][0])
        break
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
