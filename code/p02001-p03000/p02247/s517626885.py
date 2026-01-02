import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    T = SS()
    P = SS()

    len_P = len(P)
    for i in range(len(T)):
        if T[i:i+len_P] == P:
            print(i)

if __name__ == '__main__':
    resolve()

