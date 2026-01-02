import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


X,Y,A,B,C = MI()
P,Q,R = LI(),LI(),LI()

Z = [(P[i],1) for i in range(A)] + [(Q[i],0) for i in range(B)] + [(R[i],-1) for i in range(C)]
Z.sort(reverse=True)
a,b,c = 0,0,0
n = 0
ans = 0
for x in Z:
    if n == X+Y:
        break
    s,t = x
    if t == 1 and a == X:
        continue
    elif t == 0 and b == Y:
        continue
    else:
        n += 1
        ans += s
        if t == 1:
            a += 1
        elif t == 0:
            b += 1
        else:
            c += 1

print(ans)
