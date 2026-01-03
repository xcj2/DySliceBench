import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    inf = 10 ** 14
    n, m = MI()
    ee = []
    # スコアの正負を逆にし、最小値を求める問題に置き換える
    for _ in range(m):
        a, b, c = MI()
        a, b = a - 1, b - 1
        ee.append([a, b, -c])
    # ベルマン・フォードで最小スコアを計算
    # n-1回やっても更新があるということは負の閉路があるということ
    # 負の閉路がなければ答えを出力して終了
    score = [inf] * n
    score[0] = 0
    for _ in range(n):
        change = False
        for a, b, c in ee:
            if score[a] + c < score[b]:
                score[b] = score[a] + c
                change = True
        if not change:
            print(-score[n - 1])
            exit()
    # 負の閉路がある場合は、その影響がゴールまで届くかをチェック
    reachable = [False] * n
    for _ in range(n):
        for a, b, c in ee:
            if reachable[a]:reachable[b]=True
            if score[a] + c < score[b]:
                score[b] = score[a] + c
                reachable[b] = True
        if reachable[n - 1]:
            print("inf")
            exit()
    print(-score[n-1])

main()
