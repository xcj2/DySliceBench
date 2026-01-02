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
import bisect

def solve():
    n = II()
    L = LI()
    L = sorted(L)

    ans = 0
    for i in range(n):
        li = L[i]
        for j in range(i+1, n):
            lj = L[j]
            ab = li + lj
            l_idx = j + 1
            r = li + lj
            # c = [l_idx, r_idx)
            r_idx = bisect.bisect_left(L, r)
            # print(li, lj, l_idx, r_idx)
            ans += r_idx - l_idx
    print(ans)

if __name__ == '__main__':
    solve()
