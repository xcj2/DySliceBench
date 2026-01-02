import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def radian(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)

# (distance, radian)
def drx(d, r):
    return math.cos(r) * d

def dry(d, r):
    return math.sin(r) * d

def main():
    x1,y1,x2,y2 = LI()
    d = distance(x1, y1, x2, y2)
    r = radian(x1, y1, x2, y2)
    x3 = x1 + int(round(drx(d*(2**0.5), r+math.pi/4)))
    y3 = y1 + int(round(dry(d*(2**0.5), r+math.pi/4)))
    x4 = x1 + int(round(drx(d, r+math.pi/2)))
    y4 = y1 + int(round(dry(d, r+math.pi/2)))

    return '{} {} {} {}'.format(x3,y3,x4,y4)


print(main())
