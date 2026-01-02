import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    n = I()

    tmp = n
    ans = []
    factor = 2
    while factor<n**0.5 and tmp>1:
        if tmp%factor == 0:
            tmp //= factor 
            ans.append(factor)
        else:
            factor += 1
    if tmp>=2:
        ans.append(tmp)
    print(str(n)+':', ' '.join([str(i) for i in ans]))

if __name__ == '__main__':
    resolve()
