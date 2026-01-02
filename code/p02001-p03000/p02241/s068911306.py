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
     
     n=int(input())
     P=[i for i in range(n)]
     edge_CostAndVertex=[]
     for i in range(n):
          cost=list(map(int,input().split()))
          for j in range(i):
               if cost[j]!=-1:
                    edge_CostAndVertex.append([cost[j],[i,j]])
                    
     edge_CostAndVertex.sort(key=lambda x:x[0])
     ans=0
     check=[]#連結されている頂点
     main_edge=edge_CostAndVertex[0][1][0]
     for i in edge_CostAndVertex:
          cost_i,a,b=i[0],i[1][0],i[1][1]
          if is_same_set(a,b):
               continue
          else:

               unite(a,b)
               ans+=cost_i
               if a not in check:
                    check.append(a)
               if b not in check:
                    check.append(b)
               if len(check)==n:
                    flag=1
                    for i in range(n):
                         for j in range(i):
                              if is_same_set(i,j):
                                   continue
                              else:
                                   flag=0
                                   break
                    if flag==1:
                         break
                    
     print(ans)
                    
if __name__=='__main__':
     main()
