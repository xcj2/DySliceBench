# Python program to print all paths from a source to destination. 
cnt=0 
ans=0 
from collections import defaultdict 
from collections import Counter 
def check(arr): 
    c=Counter(arr)
    for i in range(n):
        if c[i]!=1:
            return 0 
    return 1 
#This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		#No. of vertices 
		self.V= vertices 
		
		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 
	def printAllPathsUtil(self, u, d, visited, path):
	   
		# Mark the current node as visited and store in path 
		visited[u]= True
		path.append(u) 
		global ans 
		# If current vertex is same as destination, then print 
		# current path[] 
		if u ==d: 
		   # print(path)
		    if check(path): 
		        ans+=1 
		else: 
			# If current vertex is not destination 
			#Recur for all the vertices adjacent to this vertex 
			for i in self.graph[u]: 
				if visited[i]==False: 
					self.printAllPathsUtil(i, d, visited, path) 
					
		# Remove current vertex from path[] and mark it as unvisited 
		path.pop() 
		visited[u]= False


	# Prints all paths from 's' to 'd' 
	def printAllPaths(self,s, d): 

		# Mark all the vertices as not visited 
		visited =[False]*(self.V) 

		# Create an array to store paths 
		path = [] 

		# Call the recursive helper function to print all paths 
		self.printAllPathsUtil(s, d,visited, path) 



# Create a graph given in the above diagram 
n,m=map(int,input().split())
g = Graph(n)
for i in range(m): 
    a,b=map(int,input().split())
    g.addEdge(a-1,b-1)
    g.addEdge(b-1,a-1)
s = 2 ; d = 3
s=0 
for d in range(0,n): 
    g.printAllPaths(s, d) 
print(ans)