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
    n = II()
    D = [[0]*10 for _ in range(10)]

    for i in range(1, n+1):
        s = list(str(i))
        l = int(s[0])
        r = int(s[-1])
        # print(s, l, r)
        D[l][r] += 1
    # print(D)

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += D[i][j] * D[j][i]
    print(int(ans))

if __name__ == '__main__':
    solve()
