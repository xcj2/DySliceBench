card = [list(map(int,input().split())) for i in range(3)]
N = int(input())
List = [int(input()) for i in range(N)]

def disclose(card, n, lst):
  for i in range(n):
    for j in range(3):
      for k in range(3):
        if card[j][k] == lst[i]:
          card[j][k] = 0
  return card
          
def trans(matrix):
  tr = []
  for i in range(len(matrix[0])):
    vector = []
    for j in range(len(matrix)):
      vector.append(matrix[j][i])
    tr.append(vector)
  return tr

def bingo(card):
  if card[0] == [0,0,0]:
    return True
  if card[1] == [0,0,0]:
    return True
  if card[2] == [0,0,0]:
    return True
  card = trans(card)
  if card[0] == [0,0,0]:
    return True
  if card[1] == [0,0,0]:
    return True
  if card[2] == [0,0,0]:
    return True
  for i in range(3):
    if card[i][i] != 0:
      break
    if i == 2:
      return True
  for i in range(3):
    if card[i][2-i] != 0:
      break
    if i == 2:
      return True
  return False
    
def judge(x):
  if x:
    return "Yes"
  return "No"

print(judge(bingo(disclose(card, N, List))))

