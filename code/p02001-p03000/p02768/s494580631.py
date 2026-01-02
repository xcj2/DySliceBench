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



def mcomb(n, k, mod):
    def mfac(l, r, mod):
        ans = l
        for i in reversed(range(r, l)):
            ans *= i
            ans %= mod
        return ans

    A = mfac(n,n-k+1,mod)
    B = mfac(k,1,mod)
    # B = mpow(B,mod-2,mod)
    B = pow(B, mod-2, mod)
    return A * B % mod

INF = float('inf')

def solve():
    n, a, b = MI()
    mod = 1000000007

    ans = pow(2, n, mod) - 1 - mcomb(n, a, mod) - mcomb(n, b, mod)
    print(ans % mod)


if __name__ == '__main__':
    solve()
