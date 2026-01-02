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
    S = list(map(int, list(input())))
 
    S = S[::-1]
    # print(S)
    n = len(S)
    mod = 2019
 
    #
    A = [0] * (n)
    a = 1
    for i in range(n):
        A[i] = S[i] * a
        a = a * 10 % mod
    # print(A)
 
    # 累積和
    R = [0] * (n+1)
    for j in range(n):
        R[j+1] = (R[j] + A[j]) % mod
    # print(R)
 
    # 個数を数える
    cnt = {}
    ans = 0
    for l in range(0, n+1):
        r = R[l]
        ans = ans + cnt.get(r, 0)
        cnt[r] = cnt.setdefault(r, 0) + 1
    print(ans)
 
if __name__ == '__main__':
    solve()