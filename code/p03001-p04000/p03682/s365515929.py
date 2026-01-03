import heapq
# n,m=map(int,input().split())
n=int(input())
def deka(a,b,c):
    return a*10**12+b*10**6+c
parents=[-1 for i in range(n)] #ひとつ親、自分が根の場合はその木のサイズ*(-1)
HEN=[] #距離が小さいものが、一番ちっちゃい数になってる
MST=[[] for i in range(n)] #答えである最小全域木
A=[]
for i in range(n):
    a,b=map(int,input().split())
    A.append([i,a,b])
A=sorted(A,key=lambda x:x[1])
for i in range(1,n):
    heapq.heappush(HEN, deka(A[i][1]-A[i-1][1],A[i][0],A[i-1][0]))
A=sorted(A,key=lambda x:x[2])
for i in range(1,n):
    heapq.heappush(HEN, deka(A[i][2]-A[i-1][2],A[i][0],A[i-1][0]))
# for i in range(m):
#     a,b,d=map(int,input().split())
#     heapq.heappush(HEN, deka(d,a,b))

def find(x): #xの最親(根)はなに？
    if parents[x] <0 : return x  #自分自身が根
    parents[x]=find(parents[x])
    return parents[x]
def union(x,y): #くっつける
    xx=find(x) ; yy=find(y)
    if xx==yy: return #xとyの根が同じ(同じグループ)ならなにもしない
    size_xx=abs(parents[xx])
    size_yy=abs(parents[yy]) #xやyの属する木のサイズ
    if size_xx>size_yy: xx,yy=yy,xx #yyの方が大きい
    parents[yy]+=parents[xx]
    parents[xx]=yy  #サイズが小さい木を大きい木に接ぐ

ans=0
while HEN:
    dd= heapq.heappop(HEN)
    d=dd//(10**12) ; a=(dd-d*10**12)//(10**6) ; b=dd%(10**6)
    if find(a)==find(b):continue
    union(a,b) #ループができるようなやつは勝手に飛ばしてくれる
    # MST[a].append(b)
    # MST[b].append(a)
    ans+=d
    #parentsは同じグループかどうかの判定用。だから経路圧縮してもよい。

print(ans)