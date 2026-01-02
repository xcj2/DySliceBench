from heapq import *
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class Dice:
    def __init__(self,top,bot,lef,rig,fro,bac):
        self.top = top
        self.bot = bot
        self.lef = lef
        self.rig = rig
        self.fro = fro
        self.bac = bac

    def up(self):
        top, bac, bot, fro = self.fro, self.top, self.bac, self.bot
        return Dice(top,bot,self.lef,self.rig,fro,bac)

    def down(self):
        top, bac, bot, fro = self.bac, self.bot, self.fro, self.top
        return Dice(top,bot,self.lef,self.rig,fro,bac)

    def right(self):
        top, rig, bot, lef = self.lef, self.top, self.rig, self.bot
        return Dice(top,bot,lef,rig,self.fro,self.bac)

    def left(self):
        top, rig, bot, lef = self.rig, self.bot, self.lef, self.top
        return Dice(top,bot,lef,rig,self.fro,self.bac)

    def state(self):
        return (self.top, self.rig, self.bot, self.lef, self.fro, self.bac)

def main():
    n=int(input())
    if n==1:
        print(1)
        print(1)
        exit()
    if n==2:
        print(2)
        print(0)
        print(11)
        exit()
    print(n-1)
    for i in range(n-1):
        print("1"+"0"*i+"1")

main()

