import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()
    A = LI()

    # color_number[i][j]: [0, i)でj番目に多い色の人数
    color_number = [[0, 0, 0] for _ in range(N)]
    for i in range(N-1):
        if A[i] in color_number[i]:
            idx = color_number[i].index(A[i])
        else:
            idx = -1
        for j in range(3):
            if j==idx:
                color_number[i+1][j] = color_number[i][j] + 1
            else:
                color_number[i+1][j] = color_number[i][j]

    ans = 1
    for i in range(N):
        ans *= color_number[i].count(A[i])
        ans %= MOD

    print(ans)

if __name__ == '__main__':
    resolve()