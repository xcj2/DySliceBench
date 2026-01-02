import sys;input=sys.stdin.readline
n=int(input())
s=input()
num=2**(n-1).bit_length()
def segfunc(x,y):return x|y
seg=[0]*(2*num-1)
for i in range(n):seg[i+num-1]=2**(ord(s[i])-97)
for i in range(num-2,-1,-1):seg[i]=segfunc(seg[2*i+1],seg[2*i+2])
def update(i,x):
  i+=num-1;seg[i]=x
  while i:i=(i-1)//2;seg[i]=segfunc(seg[i*2+1],seg[i*2+2])
def query(l,r):
  l+=num-1;r+=num-1
  if l==r:return seg[l]
  s=seg[l];l+=1
  while r-l>1:
    if ~l%2:s=segfunc(seg[l],s)
    if r%2:s=segfunc(seg[r],s);r-=1
    l//=2;r=(r-1)//2
  if l==r:return segfunc(s,seg[l])
  return segfunc(s,segfunc(seg[l],seg[r]))
for _ in range(int(input())):
  quer=input().split()
  if quer[0]=="1":
    _,i,c=quer
    update(int(i)-1,2**(ord(c)-97))
  else:
    _,l,r=quer
    print(sum(map(int,bin(query(int(l)-1,int(r)-1))[2:])))