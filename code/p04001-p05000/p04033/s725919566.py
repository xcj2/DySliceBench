# input including new line and return list of int
def get_include_new_line_input():
	pass
	N = int(input())
	a = []
	for x in range(N):
		a.append(int(input()))
	return a


# input splitted by space and return list of int
def get_spilitted_space_input():
	a = list(map(lambda x:int(x), input().split()))
	return a

# input is list of num
# output is string meaning the sign
def which_sign(a):
	if a[0] <= 0 and 0 <= a[1]:
		return 'Zero'
	elif a[0] > 0:
		return 'Positive'
	else :
		if (a[1] - a[0]) % 2 == 0:
			return 'Negative'
		else:
			return 'Positive'

if __name__ == '__main__':
	input_list = get_spilitted_space_input()
	print(which_sign(input_list))
