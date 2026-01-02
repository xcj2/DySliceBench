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

def solve():
    k, n = MI()
    A = LI()
    for i in range(n):
        A.append(k+A[i])
    # A = A * 2
    # print(A)
    S = [0] * (2 * n)

    ans = INF
    for i in range(1, 2 * n):
        # print(i)
        # S[i-1] = A[i] - A[i-1]
        S[i] = S[i-1] + A[i] - A[i-1]
        if i >= (n - 1):
            # print(S[i], S[i-n+1])
            ans = min(ans, S[i] - S[i-n+1])

    # print(S)
    print(ans)


    # R
    # for i in range(k-1, 2 * n):






if __name__ == '__main__':
    solve()
