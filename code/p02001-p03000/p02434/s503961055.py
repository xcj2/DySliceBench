from array import array
n,q = [int(i) for i in input().split()]

count = [0 for i in range(n)]
input_ = [0 for i in range(q)] 
for i in range(q):
	input_[i] = input()
	a = [int(i) for i in input_[i].split()]
	if a[0] == 0:
		count[a[1]] += 1
A = [array('i',[0 for i in range(count[j]+1)]) for j in range(n)]
cursor = [-1 for i in range(n)]

def pushBack(t, x):
	cursor[t] += 1
	A[t][cursor[t]] = x
def dump(t):
	print(*A[t][:cursor[t]+1], sep=' ')
def clear(t):
	cursor[t] = -1

for input__ in input_:
	a = [int(i) for i in input__.split()]
	if a[0] == 0:
		pushBack(a[1],a[2])
	elif a[0] == 1:
		dump(a[1])
	else:
		clear(a[1])



