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
    n, q = LI()
    nt = collections.deque()

    for _ in range(n):
        name, time = LSS()
        nt.append([name, int(time)])

    endtime = 0
    while nt:
        name, time = nt.popleft()
        if time>q:
            nt.append([name, time-q])
            endtime += q
        else:
            endtime+=time
            print(name, endtime)

if __name__ == '__main__':
    resolve()
