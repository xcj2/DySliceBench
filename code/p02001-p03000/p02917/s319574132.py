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
    B = LI()

    sm = 0
    for i in range(n):
        j = i - 1
        # print(i, j)
        if j < 0:
            a = B[i]
        elif i == n-1:
            a = B[j]
        else:
            a = min(B[i], B[j])
        sm = sm + a
    print(sm)



if __name__ == '__main__':
    solve()
