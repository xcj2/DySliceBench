# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n = II()
    A = LI()
    # print([bin(a) for a in A])
    mod = 1000000007
    ans = 0
    for i in range(0, 61):
        # i桁目が1の個数を数える
        x = 0
        for a in A:
            if (a >> i) & 1:
                x += 1
        y = n - x       # i桁目が0の個数
        # print(i, x, y)
        # XORなので x*y 通りの組み合わせ
        ans = ans + pow(2, i) * x * y % mod
    print(ans % mod)



if __name__ == '__main__':
    solve()
