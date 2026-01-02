def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())

def divisor(n): #約数
    f=[]
    d=[1]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append([i,c])
            c=0
    if n!=1:
        f.append([n,1])
    for i in range(len(f)):
        t=[]
        for j in range(1,f[i][1]+1):
            t.append(f[i][0]**j)
        for j in range(len(d)):
            for k in range(len(t)):
                d.append(d[j]*t[k])
    return sorted(d)

n=I()
div=divisor(n)
if len(div)%2==1:
    ddiv=div[len(div)//2+1:]
    ans=sum(ddiv)-len(ddiv)
else:
    if div[max(0,len(div)//2-1)]+1==div[len(div)//2]:
        if len(div)>=4:
            ddiv=div[len(div)//2+1:]
            ans=sum(ddiv)-len(ddiv)
        else:
            ans=0
    else:
        ddiv=div[len(div)//2:]
        ans=sum(ddiv)-len(ddiv)
print(ans)