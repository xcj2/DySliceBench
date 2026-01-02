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
    e = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = MI1()
        e[a].append((b, i))
        e[b].append((a, i))
    # print(e)

    ans = [0] * (n-1)
    def dfs(v, v_pre=-1, c_pre=-1):
        c = 1
        for (nv, id) in e[v]:
            if nv == v_pre: continue
            if c_pre == c: c += 1
            # v to nv color = c
            ans[id] = c
            dfs(nv, v, c)
            c += 1

    dfs(0)
    print(max(ans))
    printlist(ans)


if __name__ == '__main__':
    solve()
