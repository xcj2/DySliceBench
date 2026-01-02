import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    m, n = LI()

    # print(pow(m, n, MOD))
    def f(m, n, p):
        if n==1:
            return m
        else:
            if n%2==0:
                return (f(m, n//2, p)**2) % p
            else:
                return (f(m, n//2, p)**2*m) % p
    print(f(m, n, MOD))

if __name__ == '__main__':
    resolve()
