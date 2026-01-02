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

def printlist(lst, k='\n'): return k.join(list(map(str, lst)))
INF = float('inf')

def solve():
    l, r = MI()
    mod = 2019

    r = min(r, l+673)
    ans = 2018
    for i in range(l, r):
        for j in range(i+1, r+1):
            ans = min(ans, i * j % mod)

    print(ans)
if __name__ == '__main__':
    solve()
