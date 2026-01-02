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
    h, w = MI()
    ss = [[0 if c == "#" else int(c) for c in SI()] for _ in range(h)]
    stack=[(0,0,Dice(1,6,4,3,2,5))]
    fin=[[set() for _ in range(w)] for _ in range(h)]
    fin[0][0].add(Dice(1,6,4,3,2,5).state())
    while stack:
        i,j,d=stack.pop()
        if i==h-1 and j==w-1:
            print("YES")
            exit()
        ni,nj=i-1,j
        if i-1>=0:
            nd=d.up()
            if nd.bot==ss[ni][nj] and nd.state() not in fin[ni][nj]:
                fin[ni][nj].add(nd.state())
                stack.append((i-1,j,nd))
        ni,nj=i+1,j
        if i+1<h:
            nd=d.down()
            if nd.bot==ss[ni][nj] and nd.state() not in fin[ni][nj]:
                fin[ni][nj].add(nd.state())
                stack.append((i+1,j,nd))
        ni,nj=i,j-1
        if j-1>=0:
            nd=d.left()
            if nd.bot==ss[ni][nj] and nd.state() not in fin[ni][nj]:
                fin[ni][nj].add(nd.state())
                stack.append((i,j-1,nd))
        ni,nj=i,j+1
        if j+1<w:
            nd=d.right()
            if nd.bot==ss[ni][nj] and nd.state() not in fin[ni][nj]:
                fin[ni][nj].add(nd.state())
                stack.append((i,j+1,nd))
    print("NO")

main()

