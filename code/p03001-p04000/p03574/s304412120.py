import math,heapq,collections,sys,numpy
sys.setrecursionlimit(10**7)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

H,W = LI()
LS = []
LS.append("@"*(W+2))
for _ in range(H):
    LS.append("@" + S() + "@")
LS.append("@"*(W+2))

def count(i,j):
    c = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if LS[i+k][j+l] == "#":
                c +=1
    return c

for i in range(1,H+1):
    for j in range(1,W+1):
        if LS[i][j] == ".":
            LS[i] = LS[i][0:j] + str(count(i,j)) +  LS[i][j+1:W+2]

for i in range(1,H+1):
    print(LS[i][1:W+1])

