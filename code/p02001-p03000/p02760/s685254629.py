import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

A = [LI() for i in range(3)]
N = I()
b = [I() for i in range(N)]

B = [[0]*3 for i in range(3)]  #当たりなら1,外れなら0

for i in range(3):
    for j in range(3):
        for k in b:
            if A[i][j] == k:
                B[i][j] = 1

for i in range(3):
    if (len(set(B[i])) == 1 and B[i][0] == 1) or (len(set([B[j][i] for j in range(3)])) == 1 and B[0][i] == 1):
        print('Yes')
        exit()
if B[0][0] == 1 and B[1][1] == 1 and B[2][2] == 1:
    print('Yes')
    exit()
if B[0][2] == 1 and B[1][1] == 1 and B[2][0] == 1:
    print('Yes')
    exit()

print('No')