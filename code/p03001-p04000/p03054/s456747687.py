
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

H,W,N = map(int,input().split())
sr,sc = map(int,input().split())
S = input().rstrip()
T = input().rstrip()

taka = [('L','U'),('L','D'),('R','D'),('R','U')]
aoki = [('R','D'),('R','U'),('L','U'),('L','D')]

def sousa(x, s):
    if s == 'L':
        return [x[0], x[1]-1]
    elif s == 'R':
        return [x[0], x[1]+1]
    elif s == 'U':
        return [x[0]-1, x[1]]
    elif s == 'D':
        return [x[0]+1, x[1]]
    return x

def sousa_inv(x, s):
    if s == 'R':
        return [x[0], x[1]-1]
    elif s == 'L':
        return [x[0], x[1]+1]
    elif s == 'D':
        return [x[0]-1, x[1]]
    elif s == 'U':
        return [x[0]+1, x[1]]
    return x


def judge(x):
    if x[0]<= 0 or x[1]<=0:
        return False
    elif x[0]>H or x[1]>W:
        return False
    else:
        return True


for i in range(4):
    cur = [sr, sc]
    for s,t in zip(S,T):
        if s in taka[i]:
            cur = sousa(cur, s)
        if not judge(cur):
            print('NO')
            exit()
        if t in aoki[i]:
            cur = sousa(cur, t)
        if not judge(cur):
            cur = sousa_inv(cur, t)

print('YES')
