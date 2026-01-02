import math


def div_with_mod(x, y, mod):
    # Fermat's little theorem
    return x*pow(y, mod - 2, mod)


def comb(n, r, mod):
    # calculates C(n,r) with mod (assuming mod is prime)
    nc = n
    for rc in range(1, r):
        nc -= 1
        n = n*nc % mod
        r = r*rc % mod

    return div_with_mod(n, r, mod)


def solve():
    N = int(input())
    # ord("a") Unicode コードポイントを返す
    codepoint = ord("a")

    # たどるグラフの深さ
    i = 1
    # 標準形文字列とその次の辞書順
    ans = [["a", 1]]
    # 一つづつ潜る
    while i < N:
        # 次の深さをtmpとする
        tmp = []
        # 各ノード
        for w, j in ans:
            # 辞書順で追加していく
            for k in range(j+1):
                if k != j:
                    tmp.append([w + chr(codepoint+k), j])
                # 辞書順のインクリメント
                else:
                    tmp.append([w + chr(codepoint+k), j+1])
        ans = tmp
        i += 1

    [print(a[0]) for a in ans]

    # Solve
if __name__ == "__main__":
    solve()
