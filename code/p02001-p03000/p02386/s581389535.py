class dice:
	def __init__(self,data):
		self.faces = data
	
	def turn(self,direction):
		if direction == 'N':
			idx = [1,5,2,3,0,4]
			self.faces = [self.faces[i] for i in idx]
		elif direction == 'S':
			[self.turn('N') for i in range(3)]
		elif direction == 'E':
			idx = [3,1,0,5,4,2]
			self.faces = [self.faces[i] for i in idx]
		elif direction == 'W':
			[self.turn('E') for i in range(3)]
		elif direction == 'c':
			self.turn('N')
			self.turn('W')
			self.turn('S')

def issame(d1,d2):
	for o in 'cccWcccEcccNcccWcccWccc':
		if d1.faces == d2.faces:
			break
		else:
			d2.turn(o)
	if d1.faces == d2.faces:
		return True
	else:
		return False

if __name__ == '__main__':
	from itertools import combinations
	n = int(input())
	dices = []
	for i in range(n):
		dices.append(dice([int(s) for s in input().split()]))
	ans = True
	for d1,d2 in combinations(dices,2):
		if issame(d1,d2):
			ans = False
			break
	print({True:'Yes',False:'No'}[ans])
	