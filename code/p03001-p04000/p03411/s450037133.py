def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]
n=i1()
r=[]
b=[]
G=[[] for i in range(n*2+2)]

def add_edge(fm,to,cap):
  global G
  G[fm].append( [to,cap,len(G[to])]);
  G[to].append( [fm,0,len(G[fm])-1]);

def dfs(v,t,f,used):
	if v==t:
	  return f
	used[v] = 1
	for i in range(len(G[v])):
		e = G[v][i]
		if used[e[0]]==0 and e[1]>0:
			d = dfs(e[0], t, min(f,e[1]),used);
			if d > 0:
				e[1] -= d;
				
				G[e[0]][e[2]][1] += d
                                
				return d
			
		
	
	return 0


def max_flow(s,t):
        
	flow = 0
	while(1):
		used=[0 for i in range(2*n+2)]
		f = dfs(s, t, float("inf"),used)
		if f==0:
			return flow
		
		flow += f
	
for i in range(n):
 r.append(i2())
for i in range(n):
 b.append(i2())
for i in range(n):
 add_edge(0,i+1,1)
for i in range(n):
 add_edge(n+1+i,2*n+1,1)
for i in range(n):
 for j in range(n):
   if r[i][0]<b[j][0] and r[i][1]<b[j][1]:
       add_edge(1+i,n+1+j,1)
print(max_flow(0,2*n+1))