import sys
sys.setrecursionlimit(10*9)

n,m,k = map(int,input().split())
parent_of = [-1 for _ in range(n)]
#print(parent_of)
def root_of(x):
	if parent_of[x] < 0:
		return x
	else:
		parent_of[x] = root_of(parent_of[x])
		return parent_of[x]

def unite(x,y):
	top_root_x = root_of(x)
	top_root_y = root_of(y)
	if top_root_x == top_root_y:
		return False
	if parent_of[top_root_x] > parent_of[top_root_y]:
		top_root_x,top_root_y = top_root_y,top_root_x
	#print(parent_of[top_root_y])
	parent_of[top_root_x] += parent_of[top_root_y]
	parent_of[top_root_y] = top_root_x
	return True

def size_of(x):
		return -parent_of[root_of(x)]

def is_same(x,y):
	return root_of(x) == root_of(y)

friend_list = [-1] * n
for _ in range(m):
	a,b = map(int,input().split())
	a -= 1
	b -= 1
	friend_list[a] -=1
	friend_list[b] -=1
	unite(a,b)

for _ in range(k):
	c,d = map(int,input().split())
	c -= 1
	d -= 1
	if root_of(c) == root_of(d):
		friend_list[c] -= 1
		friend_list[d] -= 1
for i in range(n):
	friend_list[i] += size_of(i)
	#print(size_of(i))
print(*friend_list)
