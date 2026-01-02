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
    n, m = LI()
    edge = [[] for _ in range(n)]
    cc = [-1]*n

    for _ in range(m):
        s, t = LI()
        edge[s].append(t)
        edge[t].append(s)

    ccid = 0
    for i in range(n):
        if cc[i]==-1:
            stk = [i]
            cc[i] = ccid
            while stk:
                c = stk.pop()
                for n in edge[c]:
                    if cc[n]==-1:
                        stk.append(n)
                        cc[n] = ccid

            ccid += 1

    q = I()
    for _ in range(q):
        s, t = LI()
        if cc[s] == cc[t]:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    resolve()

