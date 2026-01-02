import sys
input=sys.stdin.readline

def init():
    #set_val
    #for j in range(26):
    #  for i in range(n):
    #    seg[j][i+num-1]=init_val[i]    
    #built
    for j in range(26):
      for i in range(num-2,-1,-1) :
        seg[j][i]=max(seg[j][2*i+1],seg[j][2*i+2]) 
    
def update(k,x):
    K =k+num-1
    seg[SS[k]][K] = 0
    while K:
        K = (K-1)//2
        seg[SS[k]][K] = max(seg[SS[k]][K*2+1],seg[SS[k]][K*2+2])
    K =k+num-1
    seg[x][K]=1
    while K:
      K=(K-1)//2
      seg[x][K]=max(seg[x][K*2+1],seg[x][K*2+2])
    SS[k]=x
    
def query(p,q):
  a=0
  for i in range(26):
    P =p+ num-1
    Q =q+ num-1
    res=ide_ele
    while Q-P>1:
        if P&1 == 0:
            res = max(res,seg[i][P])
        if Q&1 == 1:
            res = max(res,seg[i][Q])
            Q -= 1
        P = P//2
        Q = (Q-1)//2
    if P == Q:
        res = max(res,seg[i][Q])
    else:
        res = max(max(res,seg[i][P]),seg[i][Q])
    a=a+res
  print(a)
  return a

n=int(input())
S=input()
q=int(input())


#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[[ide_ele]*2*num for i in range(26)]


SS=[0]*num
for i in range(n):
  seg[ord(S[i])-97][i+num-1]=1
  SS[i]=ord(S[i])-97
#print(SS)
#print(seg)
init()
#print(seg)

for xx in range(q):
  SSS=list(input().split())
  #print(SSS)
  if SSS[0]=="1":
    #print(int(SSS[1])-1,ord(SSS[2])-97)
    update(int(SSS[1])-1,ord(SSS[2])-97)
  else:
    query(int(SSS[1])-1,int(SSS[2])-1)
#print(seg)