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
import math
n = I()

# N円払った
# 8パーセントの消費税がかかる
# 税抜き価格xを忘れたので、求めたい。
# xは整数とする。
# あり得る価格のうち一つを出力せよ。ただし考えられるものが存在しない場合はその旨を報告せよ。

# 普通に考えたら、n / 1.08が原価
# ただし、消費税は切り捨てとなる点に注意が必要。

x = n / 1.08
c_x = math.ceil(x)

f_n = math.floor(c_x * 1.08)

if f_n == n:
    print(c_x)
else:
    print(":(")