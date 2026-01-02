import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N = I()
A = []
for i in range(N):
    x,y = MI()
    A.append((x,y,i))

if N == 2:
    print(0.5)
    print(0.5)
    exit()


# グラハムスキャン(2次元の場合使用可能)

def area(X,Y,Z):  # 三角形の符号付き面積の2倍
    return (Y[0]-X[0])*(Z[1]-X[1])-(Y[1]-X[1])*(Z[0]-X[0])

from operator import itemgetter

def ConvexHull(A):  # Aの凸包を形成する点のリストを返す
    A = sorted(A,key=itemgetter(0,1))  # 適宜変更
    res = []
    N = len(A)
    for i in range(N):  # 下側
        a = A[i]
        while len(res) > 1 and area(res[-2],res[-1],a) <= 0:  # 適宜'>,<,>='に変更
            res.pop()
        res.append(a)
    r = len(res)
    for i in range(N-2,-1,-1):  # 上側
        a = A[i]
        while len(res) > r and area(res[-2],res[-1],a) <= 0:  # 適宜'>,<,>='に変更
            res.pop()
        res.append(a)
    return res


B = ConvexHull(A)
del B[-1]
ANS = [0]*N

from math import acos,pi

for j in range(len(B)):
    x,y,i = B[j]
    if j == 0:
        x1,y1,i1 = B[-1]
        x2,y2,i2 = B[j+1]
    elif j == len(B)-1:
        x1,y1,i1 = B[j-1]
        x2,y2,i2 = B[0]
    else:
        x1,y1,i1 = B[j-1]
        x2,y2,i2 = B[j+1]
    ANS[i] = (pi - acos(((x1-x)*(x2-x)+(y1-y)*(y2-y))/((((x1-x)**2+(y1-y)**2)*((x2-x)**2+(y2-y)**2))**.5)))/(2*pi)

print(*ANS,sep='\n')
