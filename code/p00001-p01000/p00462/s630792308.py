def search_min_route(d,n_list,m_list):
	result = 0
	n_list.sort()
	n_list.append(d)
	for m in m_list:
		result += bs_min(n_list,m)

	return result

def bs_min(n_list,m):
	left = 0
	right = len(n_list)-1
	count = 0
	while abs(right - left) != 1:
		mid = int((right - left)/2 + left)
		if n_list[mid] == m:
			return 0
		elif n_list[mid] > m:
			right = mid
		else:
			left = mid
		count += 1

	return min(abs(n_list[left]-m),abs(n_list[right]-m))


def main():
	#データの入力
	data_list = []
	d = int(input())
	while d != 0:
		n = int(input())
		m = int(input())
		n_list = []
		m_list = []
		n_list.append(0)
		for i in range(n-1):
			n_list.append(int(input()))

		for i in range(m):
			m_list.append(int(input()))

		new_list = [d,n,m,n_list,m_list]
		data_list.append(new_list)
		d = int(input())

	for data in data_list:
		print(search_min_route(data[0],data[3],data[4]))
		
		
if __name__ == '__main__':
	main()
