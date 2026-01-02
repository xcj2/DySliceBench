from collections import defaultdict, deque
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


n = I()
if n >= 1000:
    ans = 'ABD'
    if len(str(n - 999)) == 1:
        ans += '00' + str(n - 999)
    elif len(str(n - 999)) == 2:
        ans += '0' + str(n - 999)
    else:
        ans += str(n - 999)

else:
    ans = 'ABC'
    if len(str(n)) == 1:
        ans += '00' + str(n)
    elif len(str(n)) == 2:
        ans += '0' + str(n)
    else:
        ans += str(n)
print(ans[:3])
