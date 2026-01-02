import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
ac = 0
wa = 0
tle = 0
re = 0
for _ in range(N):
    t = S()
    if t == 'AC':
        ac += 1
    elif t == 'WA':
        wa += 1
    elif t == 'TLE':
        tle += 1
    elif t == 'RE':
        re += 1
print('AC x {}'.format(ac))
print('WA x {}'.format(wa))
print('TLE x {}'.format(tle))
print('RE x {}'.format(re))