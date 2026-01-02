import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return int(input())
from collections import defaultdict
import bisect

sys.setrecursionlimit(1000000000)

n = SI()
a_list = LI()

a_list =  sorted(a_list)
minus = bisect.bisect_left(a_list, 0)
minus_list = a_list[:minus]

plus_list = a_list[minus:]

ans = 0
p_i = 0
m_i = 0
if minus == 0:
    print(sum(plus_list) - 2*plus_list[0])
    minus_list = plus_list[0:1]
    plus_list = plus_list[1:]


elif minus == n:
    print(-sum(minus_list) + 2*minus_list[-1])
    plus_list = minus_list[-1:]
    minus_list = minus_list[:-1]

else:
    print(sum(plus_list) - sum(minus_list))

ans = minus_list[m_i]
m_i += 1
minus = len(minus_list)
plus = len(plus_list)


while p_i != (plus-1):
    print(ans, plus_list[p_i])
    ans = ans - plus_list[p_i]
    p_i += 1

print(plus_list[p_i], ans)
ans = plus_list[p_i] - ans

while m_i != minus:
    print(ans, minus_list[m_i])
    ans = ans - minus_list[m_i]
    m_i += 1
