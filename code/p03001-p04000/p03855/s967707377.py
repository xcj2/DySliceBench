#union-findの勉強
import sys
def find(x,par):
  #根そのものならそれを出力、そうじゃなければ上を探す
  if par[x]==x:
    return x
  else:
    return find(par[x],par)

def union(x,y,par,rank):
  x=find(x,par)
  y=find(y,par)

  if x!=y:
    #rankは属する根の番号
    if rank[x]<rank[y]:
      par[x]=y
    else:
      par[y]=x
      if rank[x]==rank[y]:
        rank[x]+=1

def same(x,y,par):
  return find(x,par)==find(y,par)

n,k,l=map(int, input().split())    
apar=[]
bpar=[]
arank=[0]*n
brank=[0]*n

for i in range(n):
  apar.append(i)
  bpar.append(i)

for i in range(k):
  p,q = map(int, input().split())
  union(p-1,q-1,apar,arank)

for i in range(l):
  p,q = map(int, input().split())
  union(p-1,q-1,bpar,brank)

#apar,bparは、次元の数
  
num=[]
d={}
for i in range(n):
  #Nが10**5オーダーなので、とりあえず10**6離してラベリング
  num.append(find(i,apar)+find(i,bpar)*10**6)
  #辞書になければ項目＋、あったら数を増やす
  if num[-1] in d:
    d[num[-1]]+=1
  else:
    d[num[-1]]=1
        
res=''
for i in range(n):
  #最初だけ空白は入れない
  if i!=0:
    res+=' '
  #Nの順番に、鉄道・道路の2つの分野で次元が両方同じだったら手段が2通りになる
  res+=str(d[num[i]])
print(res)