class Dice:
  def make_dice(self, value):
    self.face = value
  def move(self, direc):
    if direc == "N":
      self.face = [self.face[1], self.face[5], self.face[2], self.face[3], self.face[0], self.face[4]]
      return self.face
    elif direc == "E":
      self.face = [self.face[3], self.face[1], self.face[0], self.face[5], self.face[4], self.face[2]]
      return self.face
    elif direc == "S":
      self.face = [self.face[4], self.face[0], self.face[2], self.face[3], self.face[5], self.face[1]]
      return self.face
    elif direc == "W":
      self.face = [self.face[2], self.face[1], self.face[5], self.face[0], self.face[4], self.face[3]]
      return self.face
  def check_face(self, face1):
    for i in range(4):
      if face1 == self.face:
        return self.face
      else:
        self.face[1],self.face[2],self.face[4],self.face[3] = self.face[2],self.face[4],self.face[3],self.face[1]

def comp_dices(dice1,dice2,num):
  for i in range(6):
    dice2.make_dice(num)
    if i == 0:
      dice2.check_face(dice1.face)
      if dice1.face == dice2.face:
        return True
    elif i == 1:
      dice2.move("N")
      dice2.check_face(dice1.face)
      if dice1.face == dice2.face:
        return True
    elif i == 2:
      dice2.move("E")
      dice2.check_face(dice1.face)
      if dice1.face == dice2.face:
        return True
    elif i == 3:
      dice2.move("S")
      dice2.check_face(dice1.face)
      if dice1.face == dice2.face:
        return True
    elif i == 4:
      dice2.move("W")
      dice2.check_face(dice1.face)
      if dice1.face == dice2.face:
        return True
    elif i == 5:
      dice2.move("N")
      dice2.move("N")
      dice2.check_face(dice1.face)
      if dice1.face == dice2.face:
        return True
      else:
        return False

n = int(input())
num = []
dice = []
for i in range(n):
  num.append(list(map(int, input().split())))
  dice.append(Dice())
  dice[i].make_dice(num[i])

for i in range(n):
  for j in range(i+1,n):
    flag = comp_dices(dice[i],dice[j],num[j])
    if flag:
      break
  if flag:
    break

if flag:
  print("No")
else:
  print("Yes")
