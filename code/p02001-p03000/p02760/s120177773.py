import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')
import numpy as np

def solve():
    A = LLI(3)
    # print(A)
    n = II()
    C = np.array([[0, 0, 0] for _ in range(3)])
    # print(C)
    for i in range(n):
        b = II()
        for j in range(3):
            for k in range(3):
                if A[j][k] == b:
                    C[j][k] = 1

    # print(C)
    # tate, yoko
    for i in range(3):
        # print(C[i, :])
        # print(C[:, i])
        if sum(C[:, i]) == 3 or sum(C[i, :]) == 3:
            print('Yes')
            return

    # naname
    if C[0][0] + C[1][1] + C[2][2] == 3 or C[0][2] + C[1][1] + C[2][0] == 3:
        print('Yes')
        return

    print('No')



if __name__ == '__main__':
    solve()
