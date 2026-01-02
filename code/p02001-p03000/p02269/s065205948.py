import sys
input = sys.stdin.readline

if __name__ == '__main__':
  n=int(input())
  D=[0]*n
  A=[]

  def h1(x):
    return x%n

  def h2(x):
    return 1+x%(n-1)

  def h(x,i):
    return h1(x)+i*h2(x)

  def insert(x):
    i=0
    k=0
    while True:
      k=h(x,i)%n
      if D[k]==0:
        D[k]=x
        return k
      elif D[k]==x:
        return k
      i+=1

  def find(x):
    i=0
    k=0
    while i<n:
      k=h(x,i)%n
      if D[k]==x:
        return True
      elif D[k]==0:
        return False
      i+=1
    return False


  def getKey(X):
    res=''
    for x in X:
      if x=='A':
        res+='1'
      elif x=='C':
        res+='2'
      elif x=='G':
        res+='3'
      elif x=='T':
        res+='4'
    return int(res)

  for _ in range(n):
    c,x=input().strip("\n").split()
    #x=x.replace('A','1').replace('C','2').replace('G','3').replace('T','4')
    #x=int(x)
    x=getKey(x)
    if c=='insert':
      insert(x)
    else:
      A.append(find(x))
  for ans in A:
    print('yes' if ans else 'no')

