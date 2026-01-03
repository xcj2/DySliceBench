def square() : 
  
  W , H, N = tuple(map(int, input().split()))
  
  leftrange = 0
  lowrange = 0
  rightrange = W
  upperrange = H
  
  for i in range(N) : 
    x, y, a = tuple(map(int, input().split()))
    if a == 1 :
      if x > leftrange : 
        leftrange = x
    if a == 2 : 
      if x < rightrange : 
        rightrange = x
    if a == 3 :
      if y > lowrange : 
        lowrange = y
    if a == 4 : 
      if y < upperrange : 
        upperrange = y
        
  return leftrange, rightrange, lowrange, upperrange

def answer(x1, x2, y1, y2) : 
  if (x1 >= x2 or y1 >= y2) : 
    return 0
  return (x2 - x1) * (y2 - y1)

def main() : 
  leftrange, rightrange, lowrange, upperrange = square()
  print(answer(leftrange, rightrange, lowrange, upperrange))
  
  
main()
