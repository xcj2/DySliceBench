import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    """
    解答方針は正しかったが、選んだ竹のA,B,Cへの割り振り方の実装にてこずったので、
    潔く模範解答を写経することにする。
    こういう全列挙は再帰を使うと超あっさり書けるのは聞いてたけど、まだ実践力が足らぬ。。
    再帰を木構造に書き表せたら自然にdfsと結びつくのか！
    """

    def dfs(cur, a, b, c):
        if cur == N: # 全ての竹をチェックし終わった時
            if min(a, b, c) > 0: # a, b, cのどれにもベースの竹が取れている時
                return abs(a - A) + abs(b - B) + abs(c - C) - 30 # 最初の0本から1本への合成にはMP10は使わないので最後に引く
            else:
                return 10**10
        ret0 = dfs(cur + 1, a, b, c)                # curの竹を使わない時
        ret1 = dfs(cur + 1, a + L[cur], b, c) + 10  # curの竹をaに繋いだ時
        ret2 = dfs(cur + 1, a, b + L[cur], c) + 10  # curの竹をbに繋いだ時
        ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10  # curの竹をcに繋いだ時
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))





if __name__ == "__main__":
    main()
