#East[north][top] -> E
class Dice():
 East = [ [0,3,5,2,4,0]
		 ,[4,0,1,6,0,3]
		 ,[2,6,0,0,1,5]
		 ,[5,1,0,0,6,2]
		 ,[3,0,6,1,0,4]
		 ,[0,4,2,5,3,0]
		 ]
 def __init__(self,N):
  self.label = N
  self.top = 1
  self.north = 5
 def move(self,ori):
  #print(self.top,self.north,ori)
  if ori=='S':
   t = self.top
   self.top = self.north
   self.north = 7-t
  elif ori=='N':
   t = self.top
   self.top = 7-self.north
   self.north = t
  elif ori=='E':
   east = self.East[self.north-1][self.top-1]
   self.top = 7-east
  elif ori=='W':
   east = self.East[self.north-1][self.top-1]
   self.top = east
# Clockwise
  elif ori=='C': 
   east = self.East[self.north-1][self.top-1]
   self.north = east
 def gettop(self):
  return( self.label[self.top-1] )
 def getbottom(self):
  return( self.label[6-self.top] )
 def getnorth(self):
  return( self.label[self.north-1] )
 def getsouth(self):
  return( self.label[6-self.north] )
 def geteast(self):
  east = self.East[self.north-1][self.top-1]
  return( self.label[east-1] )
 def getwest(self):
  east = self.East[self.north-1][self.top-1]
  return( self.label[6-east] )

label = list(map(int, input().split() ))
D = Dice(label)
label = list(map(int, input().split() ))
E = Dice(label)

# outer loop: put all 6 faces to the top to check
sMove = 'NNNEEE'
for mi in range(len(sMove)+1):
 if D.gettop() == E.gettop() and D.getbottom() == E.getbottom():
  sRot = 'CCCC'
  for ri in range(len(sRot)):
   if D.getnorth() == E.getnorth() and D.geteast() == E.geteast() and D.getsouth() == E.getsouth() and D.getwest() == E.getwest():
    print('Yes')
    exit()
   if ri<len(sRot):
    E.move(sRot[ri])
 if mi<len(sMove):
  E.move(sMove[mi])
print('No')

