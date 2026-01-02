from collections import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n, m = MI()
to = defaultdict(list)
# dp[u][v] uを根としたときのサブツリーvの値
dp = {}

def dfs(u=0, pu=-1):
    res = 1
    for v in to[u]:
        if v == pu: continue
        res *= dfs(v, u) + 1
        res %= m
    if pu != -1: dp[(pu,u)] = res
    return res

def main():
    for _ in range(n - 1):
        x, y = map(int1, input().split())
        to[x].append(y)
        to[y].append(x)
    dfs()
    # bfsでdfsとは逆向きのdpを完成させる
    que = deque()
    que.append([0, -1])
    while que:
        u, pu = que.popleft()
        tn = len(to[u])
        # 累積積のための配列
        ll = [0] * tn
        rr = [0] * tn
        # uのサブツリーの値+1を入れる
        for i, v in enumerate(to[u]):
            ll[i] = rr[i] = dp[(u,v)] + 1
        # 左右から累積積を作る
        for i in range(1, tn):
            ll[i] = (ll[i - 1] * ll[i]) % m
            rr[tn - 1 - i] = (rr[tn - i] * rr[tn - 1 - i]) % m
        # 配列の最初or最後のために最後に1を追加
        ll += [1]
        rr += [1]
        # uの子vを根とみたときのサブツリーuの値を求める
        for i, v in enumerate(to[u]):
            if v == pu: continue
            dp[(v,u)] = (ll[i - 1] * rr[i + 1]) % m
            que.append([v, u])
    # p2D(dp)
    # 各頂点について答えを出す
    for u in range(n):
        ans = 1
        for v in to[u]:
            ans = (ans * (dp[(u,v)] + 1)) % m
        print(ans)

main()
