import math
def shell(l):
	N = len(l)
	cnt = 0
	m = int(math.log(2 * N + 1, 3))
	G = [(3 ** i - 1) // 2 for i in range(m, 0, -1)]

	for i in range(m):
		l, cnt = insert(l, G[i], cnt)

	return l, m, G, cnt

def insert(l, g, cnt):
	N = len(l)

	for i in range(g, N):
		v = l[i]
		j = i - g

		while j >= 0 and l[j] > v:
			l[j + g] = l[j]
			j -= g
			cnt += 1

		l[j + g] = v

	return l, cnt

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
	lists = list()

	for i in range(n):
		lists.append(int(input()))

	lists, m, g, cnt = shell(lists)
	print(m)
	output(g)
	print(cnt)
	for i in lists:
		print(i)



