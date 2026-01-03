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


a, b, c = LI()
if a == b == c:
    if a % 2:
        print(0)
    else:
        print(-1)
else:
    ans = 0
    while True:
        if a % 2 or b % 2 or c % 2:
            break
        a, b, c = b // 2 + c // 2, a // 2 + c // 2, a // 2 + b // 2
        ans += 1
    print(ans)
