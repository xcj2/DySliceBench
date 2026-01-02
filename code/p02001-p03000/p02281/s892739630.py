n=int(input())
nil=-1
t=[[-1,-1,-1]for _ in range(n)]
for i in range(n):
	a,b,c=map(int,input().split())
	if b!=-1:
		t[b][0]=a
		t[a][1]=b
	if c!=-1:
		t[c][0]=a
		t[a][2]=c
cnt=0
for i in range(n):
	if t[i][0]==-1:
		root=i
		break
def pre(u):
	if u==nil:
		return
	print(" "+str(u),end="")
	pre(t[u][1])
	pre(t[u][2])
def pre2(u):
	if u==nil:
		return
	pre2(t[u][1])
	print(" "+str(u),end="")
	pre2(t[u][2])
def pre3(u):
	if u==nil:
		return
	pre3(t[u][1])
	pre3(t[u][2])
	global cnt
	if cnt==n-1:
		print(" "+str(u))
	else:
		print(" "+str(u),end="")
	cnt+=1
print("Preorder")
pre(root)
print("\n"+"Inorder")
pre2(root)
print("\n"+"Postorder")
pre3(root)

