def LI(): return [int(x) for x in input().split(" ")]
def LS(): return [str(x) for x in input().split(" ")]
def ItoS(L): return [str(x) for x in L]
def StoI(L): return [int(c) for c in L]


def solve():
    n = int(input())
    A = [[], []]
    for i in range(2):
        A[i] = LI()

    for i in range(2):
        for j in range(1, n):
            A[i][j] += A[i][j - 1]

    summation = []
    summation.append(A[0][0] + A[1][n - 1])
    for i in range(1, n):
        summation.append(A[0][i] + A[1][n - 1] - A[1][i - 1])

    print(max(summation))


solve()