# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


# mathを使わない切り上げ
def ceil(n, m):
    return -(-n//m)


d, g = LI()
contest = [LI() for _ in range(d)]

ans = INF

# Bit全探索
for bit in range(1 << d):
    score = 0
    cnt = 0
    remain_max = -1

    # 各bitが立っているか確認
    for i in range(d):
        if bit >> i & 1:
            score += contest[i][0] * (i + 1) * 100 + contest[i][1]
            cnt += contest[i][0]
            continue
        # コンプリートしなかった問題の中で最も得点の高い問題をメモ
        remain_max = i

    if score >= g:
        ans = min(ans, cnt)
        continue

    need = ceil((g - score) // 100, remain_max + 1)

    if need >= contest[remain_max][0]:
        continue

    ans = min(ans, cnt + need)

print(ans)
