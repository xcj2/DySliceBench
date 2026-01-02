from collections import deque
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


s = S()
q = I()
queries = SR(q)
que = deque(list(s))
top = True  # 先頭の位置 Trueが左（初期位置）
for query in queries:
    if query[0] == '1':
        top = not(top)
    else:
        _, f, c = query.split()
        if f == '1':
            if top:
                que.appendleft(c)
            else:
                que.append(c)
        else:
            if top:
                que.append(c)
            else:
                que.appendleft(c)
if top:
    print(''.join(list(que)))
else:
    print(''.join(list(que))[::-1])
