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
a = IR(n)

# N個のボタンがあり、今1個のボタンが光っている。
# ボタンは1~Nまで番号があり、iが光っているときに押すと、iの光が消え、aiが光る。
# 光っていないボタンを押しても反応しない。
# ボタン１が光っている状態で開始、ボタン2が光っている状態で終了したい。
# そのようなことが不可能であれば－1、可能であれば最小回数を出力

#　普通にシミュレートしたらよい。
#　n回ボタン押したうえで、2にたどり着かなかったらどこかで同じボタンを2回押していることになる。

count = 0
cur = 1

while count < n:
    count += 1
    cur = a[cur-1]
    if cur == 2:
        print(count)
        sys.exit()
print(-1)