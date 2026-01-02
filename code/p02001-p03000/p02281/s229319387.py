def preOrder(s):
	print(" " + str(s),end="")
	if main[s][1] != -1:
		preOrder(main[s][1])
	if main[s][2] != -1:
		preOrder(main[s][2])

def inOrder(s):
	if main[s][1] != -1:
		inOrder(main[s][1])
	print(" " + str(s),end="")
	if main[s][2] != -1:
		inOrder(main[s][2])

def postOrder(s):
	if main[s][1] != -1:
		postOrder(main[s][1])
	if main[s][2] != -1:
		postOrder(main[s][2])
	print(" " + str(s),end="")

n = int(input())
main = [[-1] * 1 for i in range(n+1)]
for i in range(n):
	a = input().split()
	for j in range(1,3):
		main[int(a[j])][0] = int(a[0])
		main[int(a[0])].append(int(a[j]))
	#print(main)

del a


for i in range(n):
	if main[i][0] == -1:
		print("Preorder")
		preOrder(int(i))
		print()
		print("Inorder")
		inOrder(int(i))
		print()
		print("Postorder")
		postOrder(int(i))
		break
print()

#print(main)



