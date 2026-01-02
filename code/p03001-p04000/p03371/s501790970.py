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

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

def solve():
    a, b, c, x, y = MI()

    ans = INF
    for k in range(100001):
        yen = 2 * c * k + max(0, x-k) * a + max(0, y-k) * b
        ans = min(ans, yen)
    print(ans)


if __name__ == '__main__':
    solve()
