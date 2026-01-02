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

if N % 3 != 0:
    for i in range(N):
        if a[i] != 0:
            print('No')
            break
    else:
        print('Yes')
    exit()

B = list(set(a))
b = len(B)
n = N//3
if b > 3:
    print('No')
elif b == 1:
    for i in range(N):
        if a[i] != 0:
            print('No')
            break
    else:
        print('Yes')
elif b == 2:
    x,y = B
    c = a.count(x)
    d = a.count(y)
    if x != 0 and y != 0:
        print('No')
    elif x == 0:
        if c == n:
            print('Yes')
        else:
            print('No')
    else:
        if d == n:
            print('Yes')
        else:
            print('No')
else:
    x,y,z = B
    c = a.count(x)
    d = a.count(y)
    if not (c == d == n):
        print('No')
    else:
        if x ^ y == z:
            print('Yes')
        else:
            print('No')
