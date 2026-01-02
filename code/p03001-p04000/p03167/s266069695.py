from collections import deque
import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

H,W=LI()

MP=[input() for _ in range(H)]
MEMO=[[(-1,0)]*W for _ in range(H)]
MEMO[0][0] = (0,1)
QU=deque([])

QU.append((0,0,0))
IT=[(1,0),(0,1)]
while QU:
    i,j,cost = QU.popleft()
    cost+=1
    pat = MEMO[i][j][1]
    for dy, dx in IT:
        ny, nx = i+dy, j+dx
        if ny < H and ny >= 0 and nx < W and nx >= 0 and MP[ny][nx] == '.':
            cost2, pat2 = MEMO[ny][nx]
            if cost2 == -1:
                # print('i:{},j:{},ny:{},nx:{},cost:{},pat:{}'.format(i,j,ny,nx,cost,pat))
                MEMO[ny][nx] = (cost, pat)
                QU.append((ny,nx,cost))
            elif cost2 == cost:
                _pat = (pat+pat2)%DVSR
                MEMO[ny][nx] = (cost,_pat)
                # print('i:{},j:{},ny:{},nx:{},cost:{},pat:{}'.format(i,j,ny,nx,cost,_pat))
                # QU.append((ny,nx,cost,pat))
# for li in MEMO:
    # print(li)
print(MEMO[H-1][W-1][1])