#インポート
import sys

#入力用
def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def ISS(): return sys.stdin.readline().rstrip().split()
def IS(): return sys.stdin.readline().rstrip()

N, M = ISI()
A = [IS() for _ in range(N)]
B = [IS() for _ in range(M)]

def match(x, y):
    ok = True
    for i in range(M):
        for j in range(M):
            if A[x+i][y+j] != B[i][j]:
                ok = False
    return ok


find = False
for i in range(N-M+1):
    for j in range(N-M+1):
        if match(i, j) == True:
            find = True
if find == True:
    print("Yes")
else:
    print("No")