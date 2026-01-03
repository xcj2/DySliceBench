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
"""
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
"""

#D
"""
n,k = LI()
d = LI()
lis = [0,1,2,3,4,5,6,7,8,9]
for i in d:
    if i in lis:
        lis.remove(i)
n = list(str(n))
i = 0
while i < len(n):
    while int(n[i]) not in lis and n[i] != "10":
        n[i] = str(int(n[i])+1)
    if n[i] == "10":
        if i == 0:
            n[i] = "0"
            n.insert(i,"1")
        else:
            n[i-1] = str(int(n[i-1])+1)
            n[i] = "0"
            i -= 1
        i -= 1
    i += 1
for i in n:
    print(i,end = "")
print()
"""
#E
n = II()
a = LI()
ans = float("inf")
for i in range(min(a),max(a)+1):
    cos = 0
    for j in a:
        cos += (i-j)**2
    ans = min(ans, cos)
print(ans)
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
