def selection(l):
	lists = l[:]
	N = len(lists)

	for i in range(N):
		minj = i

		for j in range(i, N):
			if int(lists[j][1]) < int(lists[minj][1]):
				minj = j
		if i == minj:
			continue
		else:
			lists[i], lists[minj] = lists[minj], lists[i]

	return lists


def bubble(l):
	lists = l[:]
	N = len(lists)
	flag = 1

	while flag:
		flag = 0
		for j in range(N - 1, 1 - 1, -1):
			if int(lists[j][1]) < int(lists[j - 1][1]):
				lists[j], lists[j - 1] = lists[j - 1], lists[j]
				flag = 1

	return lists


def output(l):
	count = 0
	leng = len(l)
	for i in l:
		count += 1
		if count < leng:
			print(i, end =' ')
		else:
			print(i)




if __name__ == '__main__':
	n = int(input())
	l = input().split()
	l_1 = bubble(l)
	l_2 = selection(l)

	output(l_1)
	print("Stable")
	output(l_2)
	if l_1 == l_2:
		print("Stable")
	else:
		print("Not stable")

