import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
A = LI()

for i in range(N):
    if A[i] == 0:
        print(0)
        exit()


ans = 1
for i in range(N):
    ans *= A[i]
    if ans > 10**18:
        print(-1)
        exit()

print(ans)