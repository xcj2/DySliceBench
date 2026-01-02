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
    A = LI()

    k = max(A)
    B = [0]*(n+1)

    def CountingSort(A, B, k):
        C = [0]*(k+1)

        for j in range(n):
            C[A[j]] += 1

        for i in range(1, k+1):
            C[i] = C[i] + C[i-1]

        for j in range(n-1, -1, -1):
            B[C[A[j]]] = A[j]
            C[A[j]] -= 1

        print(*B[1:])

    CountingSort(A, B, k)

if __name__ == '__main__':
    resolve()

