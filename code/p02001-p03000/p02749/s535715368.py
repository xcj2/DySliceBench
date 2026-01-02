#####
 
import numpy as np
from numpy import int32, int8
from collections import defaultdict

#####
 
def getIntList(inp):
	return [int(_) for _ in inp]
 
 
from sys import stdin
import sys
sys.setrecursionlimit(10**6) 
def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs
 
 
def dfs(node, depths, d, connected, parent):
	depths[node-1]=d
	for child in connected[node]:
		if child==parent: continue
		dfs(child, depths, not d, connected, node)
		
 
def main(inputs):
	n=int(inputs[0][0])
	
	edge=defaultdict(list)
	for i in range(n-1):
		a,b=getIntList(inputs[1+i])
		edge[a].append(b)
		edge[b].append(a)
	
# 	for v0 in sorted(edge): print(v0, sorted(edge[v0]))
	
	depths=np.empty(n, np.bool)
	dfs(1, depths, 0, edge, -1)
# 	for i in range(n):print(i+1,depths[i])
# 	depths%=2
	
	m=n%3
	if m==0: remainingMod=[n//3,n//3,n//3]
	elif m==1: remainingMod=[n//3,n//3+1,n//3]
	elif m==2: remainingMod=[n//3,n//3+1,n//3+1]
# 	print(remainingMod)
	
	values=np.empty(n, int32)
	sum0=(depths==0).sum()
	sum1=(depths==1).sum()
	
# 	global counts
	
	if sum0<=remainingMod[0]:
# 		counts[0]+=1
		values[depths==0]=0
		remainingMod[0]-=sum0
		remaining=np.concatenate([v*np.ones(remainingMod[v], int32) for v in range(3)])
		values[depths==1]=remaining
	
	elif sum1<=remainingMod[0]:
# 		counts[1]+=1
		values[depths==1]=0
		remainingMod[0]-=sum1
		remaining=np.concatenate([v*np.ones(remainingMod[v], int32) for v in range(3)])
		values[depths==0]=remaining
		
	else:
# 		counts[2]+=1
		remaining=np.concatenate([1*np.ones(remainingMod[1], int32), np.zeros(sum0-remainingMod[1])])
		values[depths==0]=remaining
		remaining=np.concatenate([2*np.ones(remainingMod[2], int32), np.zeros(sum1-remainingMod[2])])
		values[depths==1]=remaining
	
	values[values==0]=np.arange((values==0).sum())*3+3
	values[values==1]=np.arange((values==1).sum())*3+1
	values[values==2]=np.arange((values==2).sum())*3+2
	print(" ".join(map(str,values)))
	
# 	v3=defaultdict(list)
# 	for i in range(1,n+1):
# 		visited=set([i])
# 		prev=[i]
# 		for count in range(3):
# 			next=[]
# 			for node in prev:
# 				for child in edge[node]:
# 					if child in visited: continue
# 					next.append(child)
# 			visited.update(next)
# 			prev=next
# # 			print(i, next)
# 		v3[i]=next
# 	
# # 	for v0 in sorted(v3):
# # 		print(v0, sorted(v3[v0]))
# 	
# # 	print("testing")
# 	ok=True
# 	for v0 in v3:
# 		for v1 in v3[v0]:
# 			val0=values[v0-1]
# 			val1=values[v1-1]
# 			if (val0+val1)%3==0 or (val0*val1)%3==0:
# 				pass
# # 				print(v0, val0%3, v1, val1%3, "ok")
# 			else:
# # 				print(v0, val0%3, v1, val1%3, "NG")
# 				ok=False
# 	assert ok
 
 
if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)