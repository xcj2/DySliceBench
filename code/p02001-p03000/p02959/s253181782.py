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
    B = LI()

    cnt = 0
    for i in range(n):
        left = min(A[i], B[i])
        B[i] -= left
        cnt += left

        # if B[i] > 0:
        right = min(A[i+1], B[i])
        A[i+1] -= right
        cnt += right
    print(cnt)

if __name__ == '__main__':
    solve()
