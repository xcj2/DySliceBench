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
    C = []
    for i in range(n):
        a, b = MI()
        C.append((a, b))
    C = sorted(C, key=lambda x:x[1])
    # print(C)

    ctime = 0
    for a, b in C:
        # print(a, b)
        ctime += a
        if ctime > b:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()
