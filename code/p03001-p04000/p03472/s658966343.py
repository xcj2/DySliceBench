# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def ceil(n, m):
    return -(-n//m)


n, h = LI()
A, B = [], []
for _ in range(n):
    a, b = LI()
    A.append(a)
    B.append(b)

# 2種類以上の刀を振ることはありえない
attack = max(A)
B.sort()
B.reverse()

damage = 0
ans = 0
# 攻撃力の高い順に投げる
for i in range(n):
    if damage >= h:
        break
    # 振った時の最大ダメージ >= 投げた時のダメージの場合
    # 投げるのをやめる
    if B[i] <= attack:
        break
    damage += B[i]
    ans += 1

# 消滅するまで一番攻撃力の高い刀で殴る
if damage < h:
    ans += ceil(h - damage, attack)

print(ans)
