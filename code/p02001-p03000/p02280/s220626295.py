def tree(s,pls):
	dep[s] += pls
	pls += 1
	if main[s][1] != -1:
		ju1 = tree(main[s][1],pls)
		ju1 += 1
	else:
		ju1 = 0
		hei[s] = 0
		
	if main[s][2] != -1:
		ju2 = tree(main[s][2],pls)
		ju2 += 1
	else:
		ju2 = 0
		hei[s] = 0


	if ju1 > ju2:
		ju = ju1
	else:
		ju = ju2

	del ju1
	del ju2

	#print(str(s) + ":" + str(ju))

	if ju > hei[s]:
		hei[s] = ju
	return ju

def sib(m):
	b = main[m][0]
	if b == -1:
		return -1
	elif m == main[b][1]:
		return main[b][2]
	else :
		return main[b][1]

def deg(w):
	r = 2
	if main[w][1] == -1:
		r -= 1
	if main[w][2] == -1:
		r -= 1
	
	return r



n = int(input())
main = [[-1] * 1 for i in range(n+1)]
for i in range(n):
	a = input().split()
	for j in range(1,3):
		main[int(a[j])][0] = int(a[0])
		main[int(a[0])].append(int(a[j]))
	#print(main)

del a

dep = [-1] * n
hei = [-1] * n


for i in range(n):
	if main[i][0] == -1:
		hei[i] = tree(int(i),1)
		break


for i in range(n):
	print("node " + str(i) + 
		": parent = " + str(main[i][0]) +
		", sibling = " + str(sib(i)) +
		", degree = " + str(deg(i)) +
		", depth = " + str(dep[i]) + 
		", height = " + str(hei[i]) ,end='')
	if main[i][0] == -1:
		print(", root")
	elif main[i][1] == -1 and main[i][2] == -1:
		print(", leaf")
	else:
		print(", internal node")

#print(main)
