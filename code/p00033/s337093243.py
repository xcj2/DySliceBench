import sys
sys.setrecursionlimit(100000)

def load_balls():
	LINE_NUM, TOTAL = 0, 0
	balls = []
	i = 0
	for line in sys.stdin:
		line = line.strip()
		LINE_NUM += 1
		if LINE_NUM == 1:
			TOTAL = int(line.strip())
			continue
		balls.append([int(i) for i in line.split(" ")])
		if LINE_NUM == TOTAL+1: break
	return balls

class VesselClass:

	def __init__(self):
		self.tmp = []
		self.left = [0]
		self.right = [0]

	def fill(self, balls:list):
		self.tmp = balls

	def DFS(self):
		if len(self.tmp) == 0: print("YES")
		elif self.left[-1] < self.tmp[0]:
			self.left.append(self.tmp[0])
			self.tmp.pop(0)
			self.DFS()
		elif self.right[-1] < self.tmp[0]:
			self.right.append(self.tmp[0])
			self.tmp.pop(0)
			self.DFS()
		else: print("NO")

balls_list = load_balls()
for balls in balls_list:
	Vessel = VesselClass()
	Vessel.fill(balls)
	Vessel.DFS()