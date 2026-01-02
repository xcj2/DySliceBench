def N(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[1]
  t1[1]=d1[5]
  t1[2]=d1[2]
  t1[3]=d1[3]
  t1[4]=d1[0]
  t1[5]=d1[4]
  return t1
def S(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[4]
  t1[1]=d1[0]
  t1[2]=d1[2]
  t1[3]=d1[3]
  t1[4]=d1[5]
  t1[5]=d1[1]
  return t1
def E(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[3]
  t1[1]=d1[1]
  t1[2]=d1[0]
  t1[3]=d1[5]
  t1[4]=d1[4]
  t1[5]=d1[2]
  return t1
def W(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[2]
  t1[1]=d1[1]
  t1[2]=d1[5]
  t1[3]=d1[0]
  t1[4]=d1[4]
  t1[5]=d1[3]
  return t1

n=int(input())
d=[[0 for i in range(6)] for j in range(n)]
for i in range(n):
  d[i][:]=(int(x) for x in input().split())
  dup=[x for x in set(d[i]) if d[i].count(x)==1]
  if dup:
    if dup[0]==d[i][0]:
      d[i]=E(d[i])
    elif dup[0]==d[i][1]:
      d[i]=N(d[i])
      d[i]=E(d[i])
    elif dup[0]==d[i][3]:
      d[i]=E(d[i])
      d[i]=E(d[i])
    elif dup[0]==d[i][4]:
      d[i]=S(d[i])
      d[i]=E(d[i])
    elif dup[0]==d[i][5]:
      d[i]=W(d[i])

for i in range(1,n):
  for j in range(i-1,-1,-1):
    if d[i][2]==d[j][0]:
      d[j]=E(d[j])
    elif d[i][2]==d[j][1]:
      d[j]=N(d[j])
      d[j]=E(d[j])
    elif d[i][2]==d[j][3]:
      d[j]=E(d[j])
      d[j]=E(d[j])
    elif d[i][2]==d[j][4]:
      d[j]=S(d[j])
      d[j]=E(d[j])
    elif d[i][2]==d[j][5]:
      d[j]=W(d[j])
    elif d[i][2]!=d[j][2]:
      continue

    if d[i]==d[j]:
      print("No")
      exit()

    for k in range(3):
      d[j]=N(d[j])
      if d[i]==d[j]:
        print("No")
        exit()

print("Yes")

      
