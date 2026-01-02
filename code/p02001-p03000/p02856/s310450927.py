import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    M = I()
    dc = [LI() for _ in range(M)]

    s = sum([i[0]*i[1] for i in dc])
    print((sum([i[1] for i in dc])-1)+(s-1)//9)

if __name__ == '__main__':
    resolve()
