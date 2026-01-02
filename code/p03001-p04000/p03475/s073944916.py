import sys, math
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
    N = I()
    CSF = [LI() for _ in range(N-1)]

    for i in range(N-1):
        arrival_time = 0
        for j in range(i, N-1):
            arrival_time = math.ceil(max(arrival_time, CSF[j][1])/CSF[j][2])*CSF[j][2] + CSF[j][0]
        print(arrival_time)
    print(0)

if __name__ == '__main__':
    resolve()
