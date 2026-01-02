def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [[input().split()] for _ in range(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

n,m=n1()
ps=s2(m)
OK=NG=0
d={str(i):[False,0] for i in range(1,n+1)}
for line in ps:
    num=line.split()[0]
    ans=line.split()[1]
    if d[num][0]==False:
        if ans=="AC":
            OK+=1
            d[num][0]=True
        else:
            d[num][1]+=1
for i,b in d.items():
    if b[0]:
        NG+=b[1]
print(OK,NG)