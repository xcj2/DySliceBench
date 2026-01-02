# ABC089-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
h,w,d=IL()
A=[IL() for i in range(h)]
Al=[0]*(h*w+1)
for i in range(h):
    for j in range(w):
        Al[A[i][j]]=[i,j]

rui={}
for i in range(d):
    T=[0]
    for j in range(1,h*w+1-i-d,d):
        T.append(abs(Al[j+i][0]-Al[j+d+i][0])+abs(Al[j+i][1]-Al[j+d+i][1]))
    for j in range(len(T)-1):
        T[j+1]+=T[j]
    rui[(i+1)%d]=T
q=I()
for w in range(q):
    l,r=IL()
    idx=l%d
    if idx==0:
        li=l//d-1
        ri=r//d-1
    else:
        li=l//d
        ri=r//d
    print(rui[idx][ri]-rui[idx][li])