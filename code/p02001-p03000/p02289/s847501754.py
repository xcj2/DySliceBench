import sys, heapq
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
    S = []
    while True:
        order = LSS()
        if order[0] == 'insert':
            k = int(order[1])
            heapq.heappush(S, -k)
        elif order[0] == 'extract':
            ans = - heapq.heappop(S)
            print(ans)
        else:
            break

if __name__ == '__main__':
    resolve()

