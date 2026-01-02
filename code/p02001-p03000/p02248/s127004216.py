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

    def contain(a, b):
        a = [ord(i) for i in a]
        b = [ord(i) for i in b]
        B = 10000007
        H = 100000007
        al = len(a)
        bl = len(b)
        if al>bl:
            return False

        t = pow(B, al, H)

        ah = 0
        bh = 0
        for i in range(al):
            ah = (ah * B + a[i]) % H
            bh = (bh * B + b[i]) % H

        for i in range(bl-al+1):
            if ah==bh:
                print(i)
            if i+al < bl:
                bh = (bh * B + b[i+al] - b[i] * t) % H

        return True

    contain(P, T)

if __name__ == '__main__':
    resolve()

