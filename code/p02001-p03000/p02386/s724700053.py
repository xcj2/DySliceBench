class Dice():
	def __init__(self):
		self.number = [int(i) for i in range(1,7)]
	
	def set_number(self,n0,n1,n2,n3,n4,n5):
		self.number[0] = n0
		self.number[1] = n1
		self.number[2] = n2
		self.number[3] = n3
		self.number[4] = n4
		self.number[5] = n5

	def roll(self,s):
		tmp = self.number
		if s == "S":
			self.set_number(tmp[4],tmp[0],tmp[2],tmp[3],tmp[5],tmp[1])
		elif s == "E":
			self.set_number(tmp[3],tmp[1],tmp[0],tmp[5],tmp[4],tmp[2])
		elif s == "N":
			self.set_number(tmp[1],tmp[5],tmp[2],tmp[3],tmp[0],tmp[4])
		elif s == "W":
			self.set_number(tmp[2],tmp[1],tmp[5],tmp[0],tmp[4],tmp[3])

	def get_number(self,i):
		# top: 0, front: 1, right: 2, left: 3, back: 4, bottom: 5 
		return self.number[i]

	def get_position(self,i):
		return self.number.index(i)
	
	def get_dice(self):
		return [self.number[0],self.number[1],self.number[2],self.number[3],self.number[4],self.number[5]]

def check_dice(diceA,diceB):
	dice_numA = diceA.get_dice()
	dice_numB = diceB.get_dice()
	dice_numA.sort()
	dice_numB.sort()
	if dice_numA == dice_numB:
		top = diceA.get_number(0)
		front = diceA.get_number(1)
		while diceB.get_number(1) != front:
			if diceB.get_position(front) == 2 or diceB.get_position(front) == 3:
				diceB.roll("E")
			else:
				diceB.roll("S")
		if diceB.get_number(4) != top:
			while diceB.get_number(0) != top:
				diceB.roll("E")
			if diceA.get_dice() == diceB.get_dice():
				return 0
	return 1

if __name__ == '__main__':
	num = int(input())
	dice_num = []
	for i in range(num):
		dice_num.append([int(s) for s in input().split()])

	dice = []
	for i in range(num):
		dice.append(Dice())
		dice[i].set_number(dice_num[i][0],dice_num[i][1],dice_num[i][2],dice_num[i][3],dice_num[i][4],dice_num[i][5])

	flag = 0

	for i in range(num):
		for k in range(i+1,num):
			if check_dice(dice[i],dice[k]) == 0:
				print("No")	
				exit()
	print("Yes")

