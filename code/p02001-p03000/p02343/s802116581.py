def main():
     def root(x):
          path=[]
          while x!=P[x]:
               path.append(x)
               x=P[x]
          for i in path:
               P[i]=x
          return x
     
     def is_same_set(x,y):
          return root(x)==root(y)
     
     def unite(x,y):
          P[root(x)]=root(y)
     
     n,q=map(int,input().split())
     P=[i for i in range(n)]
     for i in range(q):
          q,a,b=map(int,input().split())
          if q==0:
               unite(a,b)
          else:
               if is_same_set(a,b):
                    print(1)
               else:
                    print(0)
     
if __name__=='__main__':
     main()
