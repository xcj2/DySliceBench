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
    A = [I() for _ in range(n)]

    def insertionSort(A, n, g):
        cnt = 0
        for i in range(g, n):
            v = A[i]
            j = i-g
            while j>=0 and A[j]>v:
                A[j+g] = A[j]
                j -= g
                cnt += 1
            A[j+g] = v
        return cnt

    # shellSort(A, n)
    cnt = [0]

    G = []
    h = 1
    while h<=n:
        G.append(h)
        h = 3*h+1
    G = list(reversed(G))
    m = len(G)

    for i in range(m):
        cnt[0] += insertionSort(A, n, G[i])

    print(m)
    print(*G)
    print(cnt[0])
    for i in A:
        print(i)

if __name__ == '__main__':
    resolve()
