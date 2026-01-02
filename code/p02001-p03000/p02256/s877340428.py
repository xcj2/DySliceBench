import sys
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
    x, y = LI()

    def gcd(x, y):
        if x<y:
            x, y = y, x
        if x%y==0:
            return y
        else:
            return gcd(y, x%y)

    print(gcd(x, y))

if __name__ == '__main__':
    resolve()
