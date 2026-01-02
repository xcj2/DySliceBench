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
    N = I()
    A = LI()

    cnt = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j]<A[minj]:
                minj = j
        if i!=minj:
            A[i], A[minj] = A[minj], A[i]
            cnt+=1

    print(*A)
    print(cnt)

if __name__ == '__main__':
    resolve()

