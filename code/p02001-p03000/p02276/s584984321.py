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

    def partition(A, p, r):
        x = A[r]
        i = p-1
        for j in range(p, r):
            if A[j]<=x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    q = partition(A, 0, n-1)
    A_str = [str(i) for i in A]
    A_str[q] = '[' + A_str[q] + ']'
    print(*A_str)

if __name__ == '__main__':
    resolve()

