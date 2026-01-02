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
    n, k = LI()
    Q = [I() for _ in range(n)]

    def can_stack(p):
        s = 0
        truck_num = 1
        for i in Q:
            if s+i<=p:
                s += i
            else:
                truck_num += 1
                s = i
        return truck_num<=k

    ng = max(Q)-1
    ok = sum(Q)
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if can_stack(m):
            ok = m
        else:
            ng = m
    print(ok)

    # for i in range(20):
    #     print(i, can_stack(i))

if __name__ == '__main__':
    resolve()
