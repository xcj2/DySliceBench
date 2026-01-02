#ABC096-C
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
h,w=IL()
G=[["."]*(w+2)]
for i in range(h):
    G.append(["."]+S()+["."])
G.append(["."]*(w+2))
ret=True
#grid周り探索
for i in range(1,h):
    for j in range(1,w):
        if G[i][j]==".":
            continue
        ans=False
        for ti,tj in[[-1,0],[1,0],[0,1],[0,-1]]:
            if G[i+ti][j+tj]=="#":
                ans=True
        if not ans:
            ret=False
if ret:
    print("Yes")
else:
    print("No")