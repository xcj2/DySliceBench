import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)


def lcm(a,b):
    return (a // gcd(a,b)) * b


def func(n, c, d):
    cdlcm = lcm(c,d)
    return n//c + n//d - n//cdlcm

a,b,c,d = li()

print((b-a+1) - (func(b,c,d) - func(a-1,c,d)))