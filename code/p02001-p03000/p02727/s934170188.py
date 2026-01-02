import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

X, Y, A, B, C = MI()
P = LI()
Q = LI()
R = LI()

P.sort()
Q.sort()
R.sort()

Ans = []
for p in P:
    Ans.append(('P', p))
for q in Q:
    Ans.append(('Q', q))
for r in R:
    Ans.append(('R', r))
Ans.sort(key=lambda tup: tup[1])


Ans_text = []
for i in range(A + B + C - X - Y, A + B + C):
    Ans_text.append(Ans[i][0])

c = collections.Counter(Ans_text)

R_num = c['R']
P_num = c['P']
Q_num = c['Q']

ans = 0
cnt = 0
if c['P'] <= X and c['Q'] <= Y:
    while cnt < (X + Y):
        ans += Ans.pop()[1]
        cnt += 1
elif c['P'] > X:
    while cnt < X:
        ans += P.pop()
        cnt += 1
    while cnt < (X + Y):
        b = Ans.pop()
        if b[0] == 'P':
            continue
        else:
            ans += b[1]
            cnt += 1
else:
    while cnt < Y:
        ans += Q.pop()
        cnt += 1
    while cnt < (X + Y):
        b = Ans.pop()
        if b[0] == 'Q':
            continue
        else:
            ans += b[1]
            cnt += 1
print(ans)