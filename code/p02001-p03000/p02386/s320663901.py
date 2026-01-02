def move(dice, order):
  if order == "E":
    temp = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = temp
  elif order == "N":
    temp = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = temp
  elif order == "S":
    temp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp
  elif order == "W":
    temp = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = temp
  else:
    pass
  return dice

def roll(dice):
  temp = dice[1]
  dice[1] = dice[2]
  dice[2] = dice[4]
  dice[4] = dice[3]
  dice[3] = temp
  return dice

def judge(dice1, dice2):
  flag = True
  for i in range(6):
    if dice1[i] != dice2[i]:
      flag = False
      break
  return flag

def aresame(dice1, dice2):
  mvdice = dice2
  cnt = 0
  
  while True:
    mvdice = move(mvdice, "E")
    cnt += 1
    if dice1[0] == mvdice[0]:
      rolldice = mvdice
      cntroll = 0
      while True:
        rolldice = roll(rolldice)
        cntroll += 1
        if judge(dice1, rolldice) == True:
          return True
        if cntroll == 4:
          break
    if cnt == 4:
      break

  mvdice = dice2
  cnt = 0
    
  while True:
    mvdice = move(mvdice, "N")
    cnt += 1
    if dice1[0] == mvdice[0]:
      rolldice = mvdice
      cntroll = 0
      while True:
        rolldice = roll(rolldice)
        cntroll += 1
        if judge(dice1, rolldice) == True:
          return True
        if cntroll == 4:
          break
    if cnt == 4:
      break

  return False


import sys

n = int(input())
saikoro = [[] for i in range(n)]
for i in range(n):
  saikoro[i] = list(map(int, input().split()))

for i in range(n):
  for j in range(i+1, n):
    if aresame(saikoro[i], saikoro[j]) == True:
      print("No")
      sys.exit()
      
print("Yes")
