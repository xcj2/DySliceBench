# coding: utf-8
# ?????????????????¨????????????
class Dice(object):
	def __init__(self, L=[1, 2, 3, 4, 5, 6]):
		# ????????¶???
		self.dice = (L[1], L[4]), (L[2], L[3]), (L[0], L[5]) # x, y, z
		self.ax = [[0, False], [1, False], [2, False]]
		self.axmap = [0, 1, 2]
		self.mm = {"N": (0, 2), "S": (2, 0), "E": (1, 2), "W": (2, 1), "R": (0, 1), "L": (1, 0)}

	def rotate(self, dir):
		def rot(k, r):
			t = self.axmap[r]
			self.axmap[k], self.axmap[r] = t, self.axmap[k]
			self.ax[t][1] = not self.ax[t][1]

		rot(*self.mm[dir])

	def front(self): return self.value(0, True)
	def rear(self): return self.value(0, False)
	def right(self): return self.value(1, True)
	def left(self): return self.value(1, False)
	def top(self): return self.value(2, True)
	def bottom(self): return self.value(2, False)
	def value(self, ax, d):
		a = self.ax[self.axmap[ax]]
		return self.dice[a[0]][a[1] if d else not a[1]]

if __name__=="__main__":
	dice1 = Dice(input().split())
	dice2 = Dice(input().split())
	def tf(p, f, d):
		for _ in range(4):
			if p==f(): break
			dice1.rotate(d)
	p = dice2.top()
	f = dice1.top
	tf(p, f, "N")
	if p!=f(): tf(p, f, "E")
	
	p = dice2.front()
	f = dice1.front
	tf(p, f, "R")

	if dice1.left()==dice2.left():
		print("Yes")
	else:
		print("No")