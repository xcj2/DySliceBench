import sys, string
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
    A, B = LI()
    Str = S()

    is_ok = True
    for i, e in enumerate(Str):
        if i==A:
            if e!='-':
                is_ok = False
        else:
            if not e in string.digits:
                is_ok = False
    
    if is_ok:
        print('Yes')
    else:
        print('No')

    
if __name__ == '__main__':
    resolve()