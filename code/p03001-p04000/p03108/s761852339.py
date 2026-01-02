#!/usr/bin/env python3
N, M = map(int, input().split())
V = [[int(j)-1 for j in input().split()] for i in range(M)]
# [[1, 2], ...] -> [[0, 1], ...]
ans = [0]*M
P = [-1]*N
size = [1]*N

def unite(a, b):
	a = find(a)
	b = find(b)
	if(size[a] < size[b]):
		a,b = b,a # swap
    # if(a != b and P[a] > P[b]):
    #    a,b = b,a
	# P[a] += P[b]
	size[a] += size[b]
	P[b] = a

def find(x):
	if(P[x] < 0):
		return x
	P[x] = find(P[x])
	return P[x]

def sizef(a):
	return size[find(a)]
    # return -P[find(a)] -> when(P[c]<0), representing c is parent and how many children it has
    #					 -> when(P[c]>=0), representing who is c's parent

t = N*(N-1)//2
for i in range(M):
	ans[M-1-i] = t
	u, v = V[M-1-i]
	if(find(u) == find(v)):
		continue
	else:
		t -= sizef(u)*sizef(v)
		unite(u, v)

print(*ans, sep = "\n") # * gets value 
						# sep means separate 