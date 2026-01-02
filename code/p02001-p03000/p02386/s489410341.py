class diceClass:
	def __init__(self, valuelist):
		self.valuelist = valuelist
		self.t = valuelist[0]
		self.b = valuelist[5]
		self.n = valuelist[4]
		self.s = valuelist[1]
		self.e = valuelist[2]
		self.w = valuelist[3]

	def print(self):
		print('t={0}, b={1}, n={2}, s={3}, w={4}, e={5}'.format(self.t, self.b, self.n, self.s, self.e, self.w))

	def throw(self, direction):
		# N,S,W,E
		if direction == 'N':
			self.t, self.s, self.b, self.n = self.s, self.b, self.n, self.t
		elif direction == 'S':
			self.t, self.s, self.b, self.n = self.n, self.t, self.s, self.b
		elif direction == 'W':
			self.t, self.e, self.b, self.w = self.e, self.b, self.w, self.t
		elif direction == 'E':
			self.t, self.e, self.b, self.w = self.w, self.t, self.e, self.b

def compare(lst1, lst2):
	for i in lst1:
		if lst2.count(i) != 1:
			return False
	return True

n = int(input())
dirinput = 'WWWWSWWWWSWWWWSWWWWWSWWWWSSWWWW'
classes = []
for i in range(0,n):
	arrinput = list(map(int, input().split()))
	dice = diceClass(arrinput)
	dicresult = []
	for s in dirinput:
		dice.throw(s)
		if dicresult.count([[dice.t, dice.s], dice.e]) == 0:
			dicresult.append([[dice.t, dice.s], dice.e])
	classes.append(dicresult)

for i in range(0, len(classes)-1):
	for j in range(i+1,len(classes)):
		if compare(classes[i],classes[j]) == True:
			print('No')
			exit(0)

print('Yes')

#		print(classes[i])
#		for k in i:
#			if
#for s in dirinput:
#	dice.throw(s)
#	dice2.throw(s)
#	if dicresult1.count([[dice.t, dice.s], dice.e]) == 0:
#		dicresult1.append([[dice.t, dice.s], dice.e])
#	if dicresult2.count([[dice2.t, dice2.s], dice2.e]) == 0:
#		dicresult2.append([[dice2.t, dice2.s], dice2.e])

#print(dicresult1)
#print(dicresult2)

#for i in dicresult1:
#	if dicresult2.count(i) != 1:
#		print('No')
#		exit(0)

#print('Yes')
