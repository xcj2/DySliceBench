#!usr/bin/env python3
from collections import defaultdict
import math
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def LIR(n): return [LI() for i in range(n)]
mod = 1000000007

#A

#B

#C
n = II()
a = LI()
print(sum(a)-n)
#D
"""
s = list(S())
lis = []
sign = ["","+"]
k = 2**(len(s)-1)
d = 10-len(s)
for i in range(d):
    s.insert(0,"0")
i = 0
for a0 in range(2):
    for a1 in range(2):
        for a2 in range(2):
            for a3 in range(2):
                for a4 in range(2):
                    for a5 in range(2):
                        for a6 in range(2):
                            for a7 in range(2):
                                for a8 in range(2):
                                    if i >= k:break
                                    lis.append(s[0]+sign[a0]+s[1]+sign[a1]+s[2]+sign[a2]+s[3]+sign[a3]+s[4]+sign[a4]+s[5]+sign[a5]+s[6]+sign[a6]+s[7]+sign[a7]+s[8]+sign[a8]+s[9])
                                    i += 1
ans = 0
for i in lis:
    ans += eval(i[d:])
print(ans)
"""
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
