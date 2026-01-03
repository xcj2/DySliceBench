#-- define function ---#
def init_box(n):
	b = []
	for i in range(n):
		b.append([False, 1])

	b[0][0] = True

	return b

def move(a, b, lst):
	if lst[a][1] == 1:
		if lst[a][0]:
			lst[a][0] = False
			lst[b][0] = True
		else:
			lst[a][0] = False
	else:
		if lst[a][0]:
			lst[b][0] = True

	lst[a][1] -= 1
	lst[b][1] += 1

def count_red(lst):
	c = 0
	for i in lst:
		if i[0]:
			c += 1

	return c

#--- main ---#
N, M = input().split()
N, M = int(N), int(M)
box = init_box(N)
act = []
for i in range(M):
	x, y = input().split()
	x, y = int(x), int(y)
	act.append([x - 1, y - 1])

for i in act:
	move(i[0], i[1], box)
print(count_red(box))
