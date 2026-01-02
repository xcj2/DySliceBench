N = int(input())
X = [tuple(map(int,input().split())) for _ in range(N)]

par = [-1 for _ in range(N)]
def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x]) #経路圧縮
            return par[x]
def same(x,y):
        return find(x) == find(y)
def unite(x,y):
        x = find(x)
        y = find(y)
        #print(x, y)
        if x == y:
            return 0
        else:
          if par[x] > par[y]:
            x,y = y,x
          par[x] += par[y]
          par[y] = x
def size(x):
        return -par[find(x)]
    


y_list = [0 for _ in range(N)]
for x, y in X:
  y_list[x-1] = y-1
#print(y_list)

tp = N
rest = N
for i in range(N):
  y = y_list[i]
  if y > tp:
    continue
  rest -= 1
  #print(i,rest)
  if i + rest < N-1: #残っている時
    unite(y, tp)
  #print(i, y, rest, tp, par)
  j = y + 1
  while j < tp:
    rest -= 1
    unite(y, j) 
    #print(y, j, par)
    j += 1
  tp = y
#print(par)  
for x, y in X:
  print(size(y-1))
  
  
    
  
  
  
  