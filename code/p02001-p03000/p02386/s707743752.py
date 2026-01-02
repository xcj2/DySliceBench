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

def min_side(dice):
	num = [int(''.join([str(i) for i in dice.faces]))]
	for o in 'cccWcccEcccNcccWcccWccc':
		dice.turn(o)
		num.append(int(''.join([str(i) for i in dice.faces])))
	return min(num)

if __name__ == '__main__':
	from itertools import combinations
	n = int(input())
	dices = []
	for i in range(n):
		dices.append(dice([int(s) for s in input().split()]))
	ans = True
	mins1 = [min_side(d) for d in dices]
	mins2 = list(set(mins1))
	if len(mins1) == len(mins2):
		print('Yes')
	else:
		print('No')