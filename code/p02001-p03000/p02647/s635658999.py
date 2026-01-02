import bisect, collections, copy, heapq, itertools, math, string, sys
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
    N, K = LI()
    A = LI()

    # 全部0の最遅ケースでもlog(N)*2くらいで収束する log(2*10**5)<50
    for _ in range(min(K, 50)):
        tmp = [0] * (N + 1)
        b = [0] * (N + 1)
        for i in range(N):
            tmp[max(i - A[i], 0)] += 1
            tmp[min(i + A[i] + 1, N)] -= 1
        for i in range(N):
            b[i+1] = tmp[i] + b[i]
        for i in range(N):
            A[i] = b[i+1] 
        # print(A)

    print(*A)

if __name__ == '__main__':
    resolve()
