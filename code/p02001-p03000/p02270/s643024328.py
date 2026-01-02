def main():
	n, n_truck = map(int, input().split())
	w_list = []

	for _ in range(n):
		w_list.append(int(input()))

	print(b_search(w_list, n_truck))
 
def b_search(w_list, n_truck):
	left = max(w_list)
	right = sum(w_list)
	while left < right:
		mid = int((left+right) / 2)
		if check(w_list, n_truck, mid):
			right = mid
		else:
			mid += 1
			left = mid

	return mid


def check(w_list, n_truck, p):
	truck_count = 1
	tmp_truck = 0

	for w in w_list:
		tmp_truck += w
		if tmp_truck > p:
			truck_count += 1
			tmp_truck = w
		if truck_count > n_truck:
			return False

	return True






if __name__ == '__main__':
    main()