from collections import Counter
def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))


n = II()
eigyo_times = [LI() for _ in range(n)]
p = [LI() for _ in range(n)]
bits = []

# それぞれの時間帯で営業するorしないを全探索しても2^10通り
for i in range(2 ** 10):
    op = [0] * 10
    for j in range(10):
        if ((i >> j) & 1):
            op[10-1-j] = 1
            bits.append(op)

profit = -(10**100)
for i, bit in enumerate(bits):
    if bit == [0,0,0,0,0,0,0,0,0,0]:  # 1つ以上の時間帯で店を営業しなければならない
        continue
    tmp_profit = 0
    for j, eigyo_time in enumerate(eigyo_times):
        # joisinoお姉ちゃんと店両方が営業している時間帯の個数を求める
        count = len([k for k in range(10) if bit[k] & eigyo_time[k]])
        tmp_profit += p[j][count]
    profit = max(profit, tmp_profit)
print(profit)
