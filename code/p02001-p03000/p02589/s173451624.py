# import sys; input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**7)
# from collections import defaultdict
ALPHABET_SIZE = 26

def getlist():
	return list(map(int, input().split()))

class Node(object):
	def __init__(self, char):
		self.char = char
		self.children = {}
		self.flag = [0] * ALPHABET_SIZE

class Trie(object):
	def __init__(self):
		self.root = Node(' ')

	def _convert_char_to_num(self, char):
		return ord(char) - 97

	def insert(self, word, tail):
		res = 0 #合う値
		current = self.root
		currentFlag = [0] * ALPHABET_SIZE

		for char in word:
			char_index = self._convert_char_to_num(char)
			for i in range(ALPHABET_SIZE):
				currentFlag[i] += current.flag[i]
			res += currentFlag[char_index]
			currentFlag[char_index] = 0

			if char_index in current.children:
				current = current.children[char_index]

			# if current.children[char_index] != -1:
			# 	current = current.children[char_index]
			else:
				new_node = Node(char)
				current.children[char_index] = new_node
				current = new_node

		char_index = self._convert_char_to_num(tail)
		res += currentFlag[char_index]

		current.flag[self._convert_char_to_num(tail)] += 1

		return res

#処理内容
def main():
	N = int(input())
	L = []
	for i in range(N):
		S = input()[::-1]
		L.append([len(S), S])

	L.sort(key = lambda x:x[0])

	ans = 0
	trie = Trie()
	for val, s in L:
		s1 = s[:-1]
		tail = s[-1]
		ans += trie.insert(s1, tail)
		# print(ans)

	print(ans)

if __name__ == '__main__':
	main()
