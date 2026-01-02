import heapq as hq
def inp():
	return (int(input()))


def inlt():
	return (list(map(int,input().split())))


def insr():
	s=input()
	return (list(s[:len(s)]))


def invr():
	return (map(int,input().split()))


def subset_sum_count(arr,n,sum):
	dp=[[0 for _ in range(sum+1)] for _ in range(n+1)]
	for i in range(n+1):
		for j in range(sum+1):
			if j==0:
				dp[i][j]=1
			elif arr[i-1]<=j:
				dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j]
			else:
				dp[i][j]=dp[i-1][j]
	return dp[n][sum]


def prefix(a):
	pre=[]
	pre.append(a[0])
	for i in range(1,len(a)):
		pre.append(pre[i-1]+a[i])
	return pre

def str_to_integer_list(n):
	a=[]
	for i in range(len(n)):
		a.append(int(n[i]))
	return a
def list_to_str(l):
	s=""
	for i in l:
		s+=str(i)
	return s
def binarySearch(arr,low,high,x):
	if (high>=low):
		mid=low+(high-low)//2
		if x==arr[mid]:
			return (mid)
		elif (x>arr[mid]):
			return binarySearch(arr,(mid+1),high,x)
		else:
			return binarySearch(arr,low,(mid-1),x)
	
	return -1


def right_shift(a,s):
	return a[s:]+a[:s]


def dijkstra(s,N,E):
	visited=set()
	dist={}
	for i in range(1,N+1):
		dist[i]=1<<29
	queue=[(dist[i],i) for i in range(1,N+1)]
	hq.heappush(queue,(0,s))
	dist[s]=0
	while queue:
		d,u=hq.heappop(queue)
		if u in visited:
			continue
		#Relax all the neighbours of u
		for t in E[u]:
			v,r=t
			if dist[v]>d+r:
				dist[v]=d+r
				hq.heappush(queue,(dist[v],v))
		#Node u has been processed
		visited.add(u)
	return dist


def path(start,end,parent):
	path=[end]
	while path[-1]!=start:
		path.append(parent[path[-1]])
	path.reverse()
	return path


def bfs(graph,start,end):
	parent={}
	queue=[]
	queue.append(start)
	while queue:
		node=queue.pop(0)
		if node==end:
			return path(start,end,parent)
		for next in graph.get(node,[]):
			if node not in queue:
				parent[next]=node
				queue.append(next)


'''for _ in range(int(input())):
	n,m=list(map(int,input().split()))
	graph=[[]for _ in range(n+1)]
	distance=[-1]*(n+1)
	visited=[False]*(n+1)
	for _ in range(m):
		x,y=list(map(int,input().split()))
		graph[x].append(y)
		graph[y].append(x)'''
'''T = int(input())
for i in range(0, T):
	N, M = map(int, input().split(' '))
	graph = {}
	for j in range(1, N+1):
		graph[j] = []
	for j in range(0, M):
		x, y, r = map(int, input().split(' '))
		graph[x].append((y,r))
		graph[y].append((x,r))'''
s=insr()
t=insr()
c=0
for i in range(len(s)):
	if s[i]!=t[i]:
		c+=1
print(c)

