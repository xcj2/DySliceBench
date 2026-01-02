#!usr/bin/env python3
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def LIR(n): return [LI() for i in range(n)]

#A
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
#B

#C

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
