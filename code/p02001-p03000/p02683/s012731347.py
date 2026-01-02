N, M, X = map(int, input().split())

costlist = []
booklist = []
for i in range(0, N):
	inpt = list(map(int, input().split()))
	costlist.append(inpt[0])
	booklist.append(inpt[1:])

def bnr(n):
	lst = []
	now = n
	for i in range(0, N):
		lst.append(now%2==1)
		now = now//2
	return lst

def pow2(n):
	now = 1
	for i in range(0, n):
		now *= 2
	return now

def judge(lst):
	for i in range(0, len(lst)):
		if lst[i] < X:
			return False
	return True

mincost = 5000000000000000

for i in range(0, pow2(N)):
	cost = 0
	lst = []
	for j in range(0, M):
		lst.append(0)
	buyornot = bnr(i)
	for j in range(0, N):
		if buyornot[j]:
			cost += costlist[j]
			for k in range(0, M):
				lst[k] += booklist[j][k]
	if judge(lst) and cost<mincost:
		mincost = cost
if mincost == 5000000000000000:
	mincost = -1
print(mincost)