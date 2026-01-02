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
k = I()
x = LI()


# xy平面上の（xi, i)にボールが配置されている。つまり各行に対して必ず一つボールがある。
# これを回収する2種類のロボットA,BをN台ずつ用意している。
# Aのi代目を(0, i)に、Bのi代目を(k, i)に設置した。
# Aロボットは、x=0からスタート, Bロボットはx = kからスタートして、各行上のボールを回収して元の位置に戻る。
# 各行のロボットを起動してすべてのボールを回収するとき、ロボットの移動距離の総和の最小値を求めよ
mov = 0

for i in range(n):
    a_m = abs(0 - x[i])
    b_m = abs(k - x[i])
    if a_m < b_m:
        mov += 2 * a_m
    else:
        mov += 2 * b_m

print(mov)
