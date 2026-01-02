#!/usr/bin/env python3
# coding: utf-8
import random


class Dice() :

    mask = {'N':(1,5,2,3,0,4), 'E':(3,1,0,5,4,2),
            'W':(2,1,5,0,4,3), 'S':(4,0,2,3,5,1),'CW':(0,2,4,1,3,5)}

    way = ("N","E","W","S","CW","Nop")

    def __init__(self, data):
        self.label = data

    def move(self, data):
        if data == "Nop":
            return
        self.label = [self.label[idx] for idx in self.mask[data]]

    def get_up(self):
        return self.label[0]

    def compare_6sq(self, dice2):
        check = True
        for i in range(6):
            if self.label[i] == dice2.label[i] :
                continue
            else:
                check = False
                break

        return check
    
    def compare_4rot(self, dice2):
        ok = False
        for i in range(4):
            self.move("CW")
            if self.compare_6sq(dice2) :
                ok =True
                break
        return ok
    
    def compare(self,dice2):
        ok = False
        orderway =("Nop","E","N","E","N","E")

        for s in orderway:
            self.move(s)
            if self.compare_4rot(dice2):
                ok = True
                break
        
        return ok
    
    def check_dicelist(self, dicelist):
        
        for tdice in dicelist:
            if self.compare(tdice):
                return True

        if len(dicelist) != 1 and dicelist[0].check_dicelist(dicelist[1:]) :
            return True

        return False
    




def check_alldice(dicelist):
    return dicelist[0].check_dicelist(dicelist[1:])

length = int(input())
dicelist1 = []
for _ in range(length):
    dicelist1.append(Dice(input().split()))

if not(check_alldice(dicelist1)) :
    print ("Yes")
else:
    print ("No")

