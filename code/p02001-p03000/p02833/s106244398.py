def count_2(n):
	d = 2
	c = 1
	while d <= n:
		d *= 2
		c += 1
	
	prev_count = 0
	total_count = 0
	
	while d >= 2:
		count = n // d
#		print(">", d, count, c)
		total_count += (count - prev_count) * c
		prev_count = count
		d //= 2
		c -= 1
	
	return total_count


def count_5(n):
	d = 5
	c = 1
	while d <= n:
		d *= 5
		c += 1
	
	prev_count = 0
	total_count = 0
	
	while d >= 5:
		count = n // d
#		print(">", d, count, c)
		total_count += (count // 2 - prev_count // 2) * c
		prev_count = count
		d //= 5
		c -= 1
	
	return total_count

def count_0(n):
	if n % 2 == 0:
		count2 = count_2(n)
		count5 = count_5(n)
		return min(count2, count5)
	else:
		return 0
print(count_0(int(input())))
