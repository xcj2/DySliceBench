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
    n, m = MI()

    num = [-1] * n
    for i in range(m):
        s, c = MI()
        s -= 1
        if num[s] == -1:
            num[s] = c
        elif num[s] == c:
            continue
        else:
            print(-1)
            return

    # print(num)
    if num[0] == 0:
        if n == 1:
            print(0)
        else:
            print(-1)
        return

    if num[0] == -1:
        if n == 1:
            print(0)
            return
        else:
            num[0] = 1

    ans = ''
    for idx, i in enumerate(num):
        if i == -1:
            ans += '0'
        else:
            ans += str(i)
    print(ans)

if __name__ == '__main__':
    solve()
