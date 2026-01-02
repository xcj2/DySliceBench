import sys
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7

s = S()

# n個のオセロストーンが1列にある。長さnの文字列sで石の状態はあらわされていて、
# i番目の石が白：w、黒:bであらわされている。
# 以下の操作を行う

# iがb,i+1がwなiを一つ選び、二つとも裏返す。

# 最大でこの作業を何回行うことができるか。

# 例
# bwbwbwbwbw ⇒ wbwbwbwbwb
# bwwbbbwwwbwb　⇒　wbwbbbwwwbwb　⇒ wwbbbwwwbwb　⇒ wwbbwbwwbwb　⇒ wwbwbbwwbwb　⇒
# wwwbbbwwbwb　⇒ wwwbbwbwbwb　⇒ wwwbwbbwbwb　⇒ wwwwbbbwbwb　⇒ wwwwbbbwbwb　⇒ 

# 最終的にwwwwwwbbbbbになるので、結論としてはwを左に動かした回数をカウントすればよい。
# このカウントは、左から見て行ってwが出た位置より左のbの数を足し上げればよい。
black = 0
ans = 0
for stone in s:
    if stone == "B":
        black = black + 1
    else:
        ans = ans + black
print(ans)