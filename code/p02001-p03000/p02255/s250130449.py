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

    print(*A)
    for i in range(1, N):
        v = A[i]
        j = i-1
        while j>=0 and A[j]>v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(*A)

if __name__ == '__main__':
    resolve()
