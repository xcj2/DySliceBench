import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = [S() for i in range(N)]

a = 0
b = 0
c = 0
d = 0
for i in range(N):
    if S[i] == 'AC':
        a += 1
    elif S[i] == 'WA':
        b += 1
    elif S[i] == 'TLE':
        c += 1
    else:
        d += 1

print('AC x {}'.format(a))
print('WA x {}'.format(b))
print('TLE x {}'.format(c))
print('RE x {}'.format(d))