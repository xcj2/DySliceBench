s_a = list(x for x in input())
s_b = list(x for x in input())
s_c = list(x for x in input())

def turn_a():
  try:
    temp = s_a.pop(0)
    if temp == 'a':
      turn_a()
    elif temp == 'b':
      turn_b()
    elif temp == 'c':
      turn_c()
  except:
    print('A')
  return
 
def turn_b():
  try:
    temp = s_b.pop(0)
    if temp == 'a':
      turn_a()
    elif temp == 'b':
      turn_b()
    elif temp == 'c':
      turn_c()
  except:
    print('B')
  return

def turn_c():
  try:
    temp = s_c.pop(0)
    if temp == 'a':
      turn_a()
    elif temp == 'b':
      turn_b()
    elif temp == 'c':
      turn_c()
  except:
    print('C')
  return

turn_a()
  
