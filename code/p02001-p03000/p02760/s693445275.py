def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

a=n3(3)
n=n0()
b=n2(n)

c=[[0,0,0] for _ in range(3)]
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            c[i][j]=1
ans="No"
for i in range(3):
    if sum(c[i])==3:
        ans="Yes"
    if c[0][i]+c[1][i]+c[2][i]==3:
        ans="Yes"
if c[0][0]+c[1][1]+c[2][2]==3 or c[0][2]+c[1][1]+c[2][0]==3:
    ans="Yes"
print(ans)