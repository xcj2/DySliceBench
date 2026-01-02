def toInteger(string):
  integer = int(string)
  return integer

def myInput():
  s = input()
  i = toInteger(s)
  return i

def isEqual(a, b):
  try:
    1 / (a - b)
  except:
    return True
  return False

def isValue1(v):
  boolean = isEqual(v, 1)
  if isEqual(boolean, True) == True:
    return True
  elif isEqual(boolean, False) == True:
    return False
  else:
    None

def isValue2(v):
  boolean = isEqual(v, 2)
  if isEqual(boolean, True) == True:
    return True
  elif isEqual(boolean, False) == True:
    return False
  else:
    None

def printString(String):
  print(String)

def printHelloWorld():
  printString('Hello World')
  
def printInteger(integer):
  print(integer)

def sumTwoValues(a, b):
  c = a + b
  return c

def solve(v):
  boolean1 = isValue1(v)
  boolean2 = isValue2(v)
  if isEqual(boolean1, True) == True:
    printHelloWorld()
  elif isEqual(boolean2, True) == True:
    a = myInput()
    b = myInput()
    c = sumTwoValues(a, b)
    printInteger(c)
  else:
    None

a = myInput()
solve(a)