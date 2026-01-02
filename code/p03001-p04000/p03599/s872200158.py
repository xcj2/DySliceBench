#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/23
Solved on 2019/3/
@author: shinjisu
"""


# ABC 074 C - Sugar Water

def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0]*n
def zeros2(n, m): return [zeros(m) for i in range(n)] # obsoleted zeros((n, m))で代替
class Debug():
    def __init__(self):
        self.debug = True
 
    def off(self):
        self.debug = False
 
    def dmp(self, x, cmt=''):
        if self.debug:
            if cmt != '':
                print(cmt, ':  ', end='')
            print(x)
        return x


def prob():
    global E, F
    db = Debug()
    db.off()
    A, B, C, D, E, F = getIntList()
    db.dmp((A, B, C, D, E, F), 'A, B, C, D, E, F')
    a = F // (100 * A)
    b = F // (100 * B)
    c = F // C
    d = F // D
    db.dmp((a, b, c, d), 'a, b, c, d')
    maxConc, maxWater, maxSugar = -1.0, 0, 0
    for i in range(a+1):
        for j in range(b+1):
            water = A*i + B*j
            if water == 0:
                continue
            if water*100 >= F:  # overflow
                break
            for n in range(c+1):
                for m in range(d+1):
                    sugar = C*n + D*m
                    conc = sugar / (sugar+water*100) * 100
                    #db.dmp((maxconc, water, sugar, conc),'maxconc, water, sugar, conc')
                    if sugar/water > E:  # not all melted
                        #db.dmp('not all melted')
                        break
                    if water*100+sugar > F:  # overflow
                        #db.dmp('overflow')
                        break
                    if conc > maxConc:
                        #db.dmp('MAX UPDATED')
                        maxConc, maxWater, maxSugar = conc, water, sugar

    db.dmp((maxConc, maxWater, maxSugar),'max conc, water, sugar')
    return maxWater*100+maxSugar, maxSugar


ans = prob()
for elm in ans:
    print(elm, end=' ')
