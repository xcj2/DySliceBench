def main():
	buillist = [Building(), Building(), Building(), Building()]
	n = int(input())
	for i in range(n):
		x = input().split()
		buillist[int(x[0]) - 1].assign(int(x[1]), int(x[2]), int(x[3]))
	for b in range(4):
		for f in range(3):
			string = map(str, buillist[b].floors[f])
			string = ' '.join(string)
			buillist[b].string[f] = string
		for f in buillist[b].string:
			print(' ' + f)
		if not b == 3:
			print('####################')

class Building():
	def __init__(self):
		self.floors = [[0]*10, [0]*10, [0]*10]
		self.string = ['', '', '']

	def assign(self, f, r, v):
		self.floors[f - 1][r - 1] += v

main()

