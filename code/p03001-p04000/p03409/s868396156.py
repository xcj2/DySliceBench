#ABC091-C
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
n=I()
R=[]
B=[]
for i in range(n):
    x,y=IL()
    R.append([x,y,x+y])
for i in range(n):
    x,y=IL()
    B.append([x,y,x+y])
R.sort(key=lambda x:-x[1])
B.sort(key=lambda x:x[0])
Rb=[True]*n
Bb=[True]*n

ans=0
for i in range(n):
    bx,by,bz=B[i]
    for j in range(n):
        rx,ry,rz=R[j]
        if rx<bx and ry<by and Rb[j] and Bb[i]:
            ans+=1
            Rb[j]=False
            Bb[i]=False
print(ans)