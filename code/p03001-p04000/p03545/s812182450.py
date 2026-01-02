class Number:
  value = '0'
  negative = False
  
  def __init__(self, value, negative):
    self.value = value
    self.negative = negative
    
  def __int__(self):
    x = int(self.value)
    return -x if self.negative else x
  
  def __str__(self):
    x = str(self.value)
    return '-' + x if self.negative else '+' + x
  
correct = []  

def solve(numbers, k):
  global correct
  if k >= len(numbers):
    if sum([int(x) for x in numbers]) == 7:
      correct.append(numbers)      
    return
  
  negative = []
  for i, x in enumerate(numbers):
    if i == k:
      negative.append(Number(x.value, True))
    else:
      negative.append(x)
  
  solve(numbers, k + 1)
  solve(negative, k + 1)
  
numbers = [Number(x, False) for x in input()] 

solve(numbers, 1)

print(''.join([str(x) for x in correct[0]])[1:] + '=7')
