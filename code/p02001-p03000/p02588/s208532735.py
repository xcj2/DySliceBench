import decimal
class Imos_2:
    def __init__(self,W,H):
        self.width=W
        self.height=H
        self.list=[[0]*(W+1) for _ in range(H+1)]

    def Add(self,F,T,C=1):
        Fx,Fy=F
        Tx,Ty=T

        self.list[Fx][Fy]+=C
        self.list[Fx][Ty+1]-=C
        self.list[Tx+1][Fy]-=C
        self.list[Tx+1][Ty+1]+=C

    def Cumulative_Sum(self):
        Y=[[0]*(self.height+1) for _ in range(self.width+1)]

        for x in range(self.width+1):
            S=0
            for y in range(self.height+1):
                S+=self.list[x][y]
                Y[x][y]=S

        for y in range(self.height+1):
            S=0
            for x in range(self.width+1):
                S+=Y[x][y]
                Y[x][y]=S

        return Y
#================================================
def f(N):
    R=[]
    for k in [2,5]:
        X=N
        Y=0
        while X%k==0:
            X//=k
            Y+=1
        R.append(min(Y,2*Max_power))
    return R

N=int(input())
Max_power=9
A=[0]*N
I=Imos_2(2*Max_power+1,2*Max_power+1)
Power=[0]*N

for i in range(N):
    A[i]=int(decimal.Decimal(input())*(10**Max_power))

for i in range(N):
    (p,q)=f(A[i])
    Power[i]=(p,q)
    I.Add((2*Max_power-p,2*Max_power-q),(2*Max_power,2*Max_power))

J=I.Cumulative_Sum()

Ans=0
for i in range(N):
    p,q=Power[i]
    Y=J[p][q]

    if (p>=Max_power) and (q>=Max_power):
        Y-=1

    Ans+=Y

print(Ans//2)
