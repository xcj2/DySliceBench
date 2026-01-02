# encoding:utf-8
def needs(n_row, n_col):
	if n_row % 2 + n_col % 2 == 0:
		return [(n_row // 2) * (n_col // 2), 0, 0]
	elif n_row % 2 + n_col % 2 == 2:
		return [(n_row // 2) * (n_col // 2), (n_row // 2) + (n_col // 2), 1]
	elif n_row % 2 == 1:
		return [(n_row // 2) * (n_col // 2), n_col // 2, 0]
	else:
		return [(n_row // 2) * (n_col // 2), n_row // 2, 0]

def alphabetCount(input_lines):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	counter = [0, 0, 0]
	for i in range(26):
		count = input_lines.count(alphabet[i])
		counter[0] += count // 4
		counter[1] += (count % 4) // 2
		counter[2] += count % 2
	return counter

def judge(needs, counter):
	if needs[0] <= counter[0] and needs[2] == counter[2]:
		return "Yes"
	else:
		return "No"


def main():
	nums = list(map(int, input().split()))
	input_lines = "".join([input() for _ in range(nums[0])])
	print(judge(needs(nums[0], nums[1]), alphabetCount(input_lines)))


if __name__ == '__main__':
	main()