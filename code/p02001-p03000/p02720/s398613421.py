def create_mapper():
	# 1 -> [0,1,2]
	# 2 -> [1,2,3]
	# 3 -> [2,3,4]
	# 4 -> [3,4,5]
	# ...
	# 8 -> [7,8,9]
	# 9 -> [8,9]
	# 0 -> [0,1]
	res = [[]]*10
	for i in range(0, 10):
		if 1 <= i <= 8:
			res[i] = [i-1, i, i+1]
		elif i == 9:
			res[i] = [8, 9]
		elif i == 0:
			res[i] = [0, 1]
	return res
mapper = create_mapper()

def map_list(lst, level):
	res = lst[::1]
	while not all([len(elem) == level for elem in res]):
		new_res = []
		for elem in res:
			if len(elem) < level:
				tmp = []
				for digit in mapper[int(elem[-1])]:
					tmp.append(elem + str(digit))
				new_res += tmp
				# print(tmp)
		res = new_res[::1]
		# print(res)
		# break
	return res

def create_lun():
	res = [i for i in range(1, 10)]
	# max_num = lunlun digit 100000 == 3234566667 <- constraint
	for depth in range(2, 11): # 2 digit to 10 digit
		tmp = [str(i) for i in range(1, 10)] # start with depth = 2
		tmp = map_list(tmp, depth)
		tmp = sorted(list(map(int, tmp)))
		res += tmp
		# print(tmp)
	# print(res[100000-1] == 3234566667)
	return res
table = create_lun()
k = int(input())
print(table[k-1])