import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,M = MI()

if N == 1:
    ans = -1
    for i in range(M):
        s,c = MI()
        if ans == -1:
            ans = c
        elif c != ans:
            print(-1)
            break
    else:
        if M != 0:
            print(ans)
        else:
            print(0)
    exit()


ANS = [-1]*N
for i in range(M):
    s,c = MI()
    if ANS[s-1] == -1:
        ANS[s-1] = c
    elif ANS[s-1] != c:
        print(-1)
        exit()

for i in range(N):
    if i == 0 and ANS[i] == 0:
        print(-1)
        exit()
    elif i == 0 and ANS[i] == -1:
        ANS[i] = '1'
    elif ANS[i] == -1:
        ANS[i] = '0'
    else:
        ANS[i] = str(ANS[i])

print(''.join(ANS))
