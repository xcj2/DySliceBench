import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


A = [LI() for _ in range(3)]
N = I()
flag = [[0]*3 for _ in range(3)]

for i in range(N):
    b = I()
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                flag[j][k] = 1

for i in range(3):
    if flag[i][0] == flag[i][1] == flag[i][2] == 1 or flag[0][i] == flag[1][i] == flag[2][i] == 1:
        print('Yes')
        exit()

if flag[0][0] == flag[1][1] == flag[2][2] == 1 or flag[0][2] == flag[1][1] == flag[2][0] == 1:
    print('Yes')
    exit()

print('No')
