import sys
from collections import deque

def convert_a_to_i(char):

	if char == 'A':
		return 1

	elif char == 'C':
		return 2

	elif char == 'G':
		return 3

	else:
		return 4

def hash_calc(word):

	hash = 0
	p = 1
	for i in range(len(word)):

		hash += convert_a_to_i(word[i]) * p
		p *= 5

	return hash

def find(dictionary,word):

	if dictionary[hash_calc(word)-1] == 1:
		return True
	else:
		return False

def insert(dictionary,word):

	dictionary[hash_calc(word)-1] = 1

def test():

	n = int(sys.stdin.readline())

	dictionary = [0] * (4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4)


	for i in range(n):

		operation = list(sys.stdin.readline().split())

		if operation[0] == 'insert':

			insert(dictionary,operation[1])
		else:

			result = find(dictionary,operation[1])
			if result == True:
				print("yes")
#				with open("out.txt",mode='a') as f:
#					f.write("yes " + operation[1] + "\n")
			else:
				print("no")
#				with open("out.txt",mode='a') as f:
#					f.write("no " + operation[1] + "\n")


if __name__ == "__main__":
	test()

