import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
a = LI()

ANS = [0]*(10**5+1)
for i in range(N):
    b = a[i]
    if b == 0:
        ANS[b] += 1
        ANS[b+1] += 1
    else:
        ANS[b-1] += 1
        ANS[b] += 1
        ANS[b+1] += 1
print(max(ANS))
