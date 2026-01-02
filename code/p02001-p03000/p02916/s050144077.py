# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n = II()
    A = LI1()
    B = LI()
    C = LI()

    # print(A)
    # print(B)
    # print(C)
    pre = -4
    ans = 0
    for a in A:
        score = B[a]
        if a - pre == 1:
            score += C[pre]
        ans += score
        pre = a
    print(ans)


if __name__ == '__main__':
    solve()
