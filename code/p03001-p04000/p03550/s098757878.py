import sys
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**7)

def main():
    N, Z, W = map(int, input().split())
    A = list(map(int, input().split()))
    """
    O(N^2)dpでも行けるそうです。以下写経：
    https://atcoder.jp/contests/abc078/submissions/14886969
    dp[turn][top]の２引数だけでいいのか、[x][y]の２引数も必要ではないかと思うが、
    考えてみれば
        dfs(0, top, x, y) = dfs(1, top', A[top], y)
                          = dfs(0, top", A[top], A[top'])
    となるので、実はdfs(0, top, x, y)はtop = Nでない限りx, yに依らない。
    """
    dp = [[-1] * N for _ in range(2)]
    def dfs(turn, top, x, y): # turn: 0 => x, 1 => y
        if top == N: return abs(x - y)
        if dp[turn][top] != -1: return dp[turn][top]
        if turn == 1:
            """
            yのターンは、top以降を取ってなるべくスコアが低くなるようなiを選ぶ
            """
            ret = 10**9
            for i in range(top, N): ret = min(ret, dfs(0, i + 1, x, A[i]))
            dp[turn][top] = ret
            return ret
        else:
            """
            xのターンは、top以降を取ってなるべくスコアが高くなるようなiを選ぶ
            """
            ret = 0
            for i in range(top, N): ret = max(ret, dfs(1, i + 1, A[i], y))
            dp[turn][top] = ret
            return ret
    
    print(dfs(0, 0, Z, W))

if __name__ == "__main__":
    main()
