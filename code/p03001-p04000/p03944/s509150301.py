
def myAnswer(W:int,H:int,N:int,X:list,Y:list,A:list) -> int:
   startX = 0
   endX = W
   startY = 0
   endY = H
   for x,y,a in zip(X,Y,A):
      if(a == 1):
         startX = max(startX,x)
      elif(a == 2):
         endX = min(endX,x)
      elif(a == 3):
         startY = max(startY,y)
      elif(a == 4):
         endY = min(endY,y)
   # print(startX,endX,startY,endY)
   return 0 if(startX > endX or startY > endY) else (endX - startX) * (endY - startY)

def modelAnswer():
   return
def main():
   W,H,N = map(int,input().split())
   X = []
   Y = []
   A = []
   for _ in range(N):
      x,y,a = map(int,input().split())
      X.append(x)
      Y.append(y)
      A.append(a)
   print(myAnswer(W,H,N,X,Y,A))
if __name__ == '__main__':
   main()