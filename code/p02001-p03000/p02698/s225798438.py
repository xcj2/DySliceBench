import sys
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(2*10**5)
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    repn = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        repn[u - 1].append(v - 1)
        repn[v - 1].append(u - 1)
    
    length = [0] * (N + 1)
    dp = [-1]

    """
    やはり各頂点でLIS配列を取ると配列コピーの時間がかかってTLEするので、
    配列は唯一つを扱って、DFSからバックするときに配列も元に戻す操作を行いたい
    （ここの実装の仕方がわからなかった）

    これはdfsを再帰で書いた後に復元操作を追記すれば異常に楽に書ける。。。
    """

    def dfs(v, p=N):
        if A[v] > dp[-1]:
            dp.append(A[v])
            length[v] = length[p] + 1
            for u in repn[v]:
                if u == p: continue
                dfs(u, v)
            dp.pop()
        else:
            length[v] = length[p]
            idx = bisect_left(dp, A[v]) # bisect_rightだとdpに重複する値を書き込んでしまうのでダメ
            old = dp[idx]
            dp[idx] = A[v]
            for u in repn[v]:
                if u == p: continue
                dfs(u, v)
            dp[idx] = old
        #print("v={}, len={}, dp={}".format(v, length[v], dp))

    dfs(0)
    length.pop()
    for ans in length:
        print(ans)
    


if __name__ == "__main__":
    main()
