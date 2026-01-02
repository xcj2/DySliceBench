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

n = I()
a = LI()

# n枚のカードでaとbが勝負。
# i番目のカードにはaiの整数が書かれている。
# それぞれ1枚ずつカードをとる。aが先行してカードをとる。
# 2人がすべてのカードをとったときゲーム終了、合計数がそれぞれの特典。
# 二人とも自分の特典を最大化するとき、AがBより何点多く取るか。
# つまりカードが見えている。

a.sort(reverse=True)
A = 0
B = 0

for i in range(n):
    if i % 2 == 0:
        A += a[i]
    else:
        B += a[i]

print(A - B)
    
