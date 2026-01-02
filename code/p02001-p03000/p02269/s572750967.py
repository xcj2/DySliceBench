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
    n = I()
    Q = [LSS() for _ in range(n)]

    d = set()

    for i, j in Q:
        if i=='insert':
            d.add(j)
        else:
            if j in d:
                print('yes')
            else:
                print('no')

if __name__ == '__main__':
    resolve()
