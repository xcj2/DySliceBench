n=int(input())+1
w = input()
data=[0]*n*2
def update(i,x):
    i+=n
    data[i]=x
    i//=2
    while i:
      data[i]=data[i*2]|data[i*2+1]
      i//=2
def query(l,r):
    l+=n
    r+=n
    s=0
    while l<r:
      if l&1 == 1:
        s|=data[l]
        l+=1
      if r&1 == 1:
        r-=1
        s|=data[r]
      l//=2
      r//=2
    return bin(s).count('1')
def word_num(a):
    return 1<<(ord(a)-97)

for i in range(n-1):
    data[i+n] = word_num(w[i])    
for i in range(n-1,0,-1):
    data[i]=data[i*2]|data[i*2 + 1]

ans=[]
q=int(input())
for i in range(q):
    a,s,t=input().split()
    if a=='1':
        s=int(s)
        update(int(s)-1,word_num(t))
    if a=='2':
        s=int(s)
        t=int(t)
        ans.append(query(int(s)-1,int(t)))
for i in range(len(ans)):
    print(ans[i])