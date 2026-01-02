import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
r = 0
left,right = [],[]

Q = I()
for i in range(Q):
    A = LS()
    if A[0] == '1':
        r = 1-r
    else:
        f,c = A[1],A[2]
        if (r == 0 and f == '1') or (r == 1 and f == '2'):
            left.append(c)
        else:
            right.append(c)

if r == 0:
    left.reverse()
    print(''.join(left+S+right))
else:
    S.reverse()
    right.reverse()
    print(''.join(right+S+left))


