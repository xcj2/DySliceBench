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
    n = II()
    S = list(input())
    # print(S)
    n = len(S)

    R = []
    G = []
    B = []
    rcnt = 0
    gcnt = 0
    bcnt = 0
    for idx, s in enumerate(S):
        if s == 'R':
            R.append(idx+1)
            rcnt += 1
        elif s == 'G':
            G.append(idx+1)
            gcnt += 1
        else:
            B.append(idx+1)
            bcnt += 1
    # print(R)
    # print(G)
    # print(B)
    ans = rcnt * gcnt * bcnt
    # print(ans)

    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            # print(i, j, k)
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)





if __name__ == '__main__':
    solve()
