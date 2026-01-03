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

a, b, c = LI()

# ABCの3人が持っているクッキーを交換する。
# 3人は同時に、手持ちのクッキーを半分割し、残りの二人にそれぞれ1方を渡すことを繰り返す。
# 誰かの持っているクッキーが奇数個になったら操作をやめる。
# クッキー交換は何回行うことができるか。無限に続けられることもある。

def distribute(a,b,c):
    x = a/2
    y = b/2
    z = c/2

    a2 = y + z
    b2 = x + z
    c2 = x + y

    if a == a2 and b == b2 and c == c2:
        print(-1)
        sys.exit()
    return a2, b2, c2

count = 0

while (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    a, b, c = distribute(a, b, c)
    count += 1
    # print(a, b, c)

print(count)