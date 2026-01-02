class Dice:	
	def __init__( self, nums ):
		self.face = nums
	
	def rolltoTopIndex( self, faceindex ):	
		if faceindex == 1:
			self.roll( "N" )
		elif faceindex == 2:
			self.roll( "W" )
		elif faceindex == 3:
			self.roll( "E" )
		elif faceindex == 4:
			self.roll( "S" )
		elif faceindex == 5:
			self.roll( "NN" )
	
	def roll( self, actions ):
		for act in actions:
			t = 0
			if act == "E":
				t =   self.face[0]
				self.face[0] =   self.face[3]
				self.face[3] =   self.face[5]
				self.face[5] =   self.face[2]
				self.face[2] = t
			elif  act == "N":
				t =   self.face[0]
				self.face[0] =   self.face[1]
				self.face[1] =   self.face[5]
				self.face[5] =   self.face[4]
				self.face[4] = t
			elif  act == "S":
				t =  self.face[ 0]
				self.face[0] =  self.face[4]
				self.face[4] =  self.face[5]
				self.face[5] =  self.face[1]
				self.face[1] = t	
			elif  act == "W":
				t =  self.face[0]
				self.face[0] =  self.face[2]
				self.face[2] =  self.face[5]
				self.face[5] =  self.face[3]
				self.face[3] = t	
			elif  act == "M":
				t =  self.face[1]
				self.face[1] =  self.face[2]
				self.face[2] =  self.face[4]
				self.face[4] =  self.face[3]
				self.face[3] = t

def isDiffDice( dice1, dice2 ):
	diceface = dice2.face
	cnt = 0
	for i in range( 6 ):
		if dice1.face[0] == dice2.face[i]:
			dice2.rolltoTopIndex( i )
			for j in range( 1, 5 ):
				if dice1.face[1] == dice2.face[1]:
					cnt = 0
					for k in range( 6 ):
						if dice1.face[k] == dice2.face[k]:
							cnt += 1
					if cnt == 6:
						break
				dice2.roll( "M" )
		if cnt == 6:
			break
		dice2.face = diceface
			
	if cnt == 6:
		return False
	else:
		return True


n = int( input( ) )
dices = [ Dice( [ int( val ) for val in input( ).split( " " ) ] ) for i in range( n ) ]

isdiff = True
for i in range( 0, n-1 ):
	for j in range( i+1, n ):
		if not isDiffDice( dices[i], dices[j] ):
			print( "No" )
			isdiff = False
			break
	if not isdiff:
		break

if isdiff:
	print( "Yes" )