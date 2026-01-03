#067-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return input()

n=I()
nl=[[] for i in range(n)]
distfen=[-1 for i in range(n)]
distsnu=[-1 for i in range(n)]

for i in range(n-1):
    a,b=IL()
    nl[a-1].append(b-1)
    nl[b-1].append(a-1)
    
q=[[0,0]]
vis=[False for i in range(n)]
while len(q)!=0:
    s,d=q.pop(0)
    vis[s]=True
    for v in nl[s]:
        if not vis[v]:
            distfen[v]=d+1
            q.append([v,d+1])

q=[[n-1,0]]
vis=[False for i in range(n)]
while len(q)!=0:
    s,d=q.pop(0)
    vis[s]=True
    for v in nl[s]:
        if not vis[v]:
            distsnu[v]=d+1
            q.append([v,d+1])
        
fen=0
snu=0

for i in range(1,n-1):
    if distfen[i]<=distsnu[i]:
        fen+=1
    else:
        snu+=1

if fen>snu:
    print("Fennec")
else:
    print("Snuke")