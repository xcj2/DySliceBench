def CP(a,b):
	x = a[1]*b[2]-a[2]*b[1]
	y = a[2]*b[0]-a[0]*b[2]
	z = a[0]*b[1]-a[1]*b[0]
	return (x,y,z)

minus = lambda d:tuple(-i for i in d)

class dice:
	def __init__(self,data):
		names = [(1,0,0),(0,0,1),(0,1,0),(0,-1,0),(0,0,-1),(-1,0,0)]
		self.faces = {n:d for n,d in zip(names,data)}
		self.top = (1,0,0)
		self.north = (0,0,-1)
	
	def turn(self,direction):
		if direction == 'N':
			self.top,self.north = minus(self.north),self.top
		elif direction == 'S':
			[self.turn('N') for i in range(3)]
		elif direction == 'W':
			self.top = CP(self.top,self.north)
		elif direction == 'E':
			[self.turn('W') for i in range(3)]

if __name__ == '__main__':
	data = [int(i) for i in input().split()]
	operations = input()
	d = dice(data)
	[d.turn(o) for o in operations]
	print(d.faces[d.top])