import sys

def jisin(gen,mae,huka):
    hukasa[gen]=huka
    for c in tens[gen]:
        if(c!=mae):
            jisin(c,gen,huka+1)
    return

def kyokudai(gen,mae):
    dai=0
    if(len(tens[gen])==1 and mae!=-1):
        dai=hukasa[gen]
        #print(dai)
    else:
        for c in tens[gen]:
            if(c!=mae):
                dai=max(dai,kyokudai(c,gen))
    saisin[gen]=dai
    #print(gen,dai)
    return dai

def oikake(gen):
    miti.append(gen)
    if(hukasa[gen]==0):
        return
    for c in tens[gen]:
        if(hukasa[c]==hukasa[gen]-1):
            oikake(c)

sys.setrecursionlimit(10**6)
n,u,v=map(int,input().split())
u-=1
v-=1
tens=[[]for i in range(n)]
hukasa=[0]*n
saisin=[0]*n

for i in range(n-1):
    s,t=map(int,input().split())
    tens[s-1].append(t-1)
    tens[t-1].append(s-1)

#print(tens)

jisin(v,-1,0)
#print(hukasa)
kyokudai(v,-1)
#print(saisin)

miti=[]
oikake(u)
l=len(miti)-1
#print(miti)
#print(l)

ans=saisin[miti[l//2]]
print(ans-1)