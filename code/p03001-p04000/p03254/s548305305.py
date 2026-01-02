def myAnswer(N:int,x:int,A:list) -> int:
   if(sum(A)==x): return N
   A.sort()
   counter = 0
   hantei = True
   for n,a in enumerate(A):
      if(a > x):
         hantei = False
         break
      elif(a == x):
         counter += 1
         return counter
      elif(a < x):
         x -= a
         counter += 1

   if(x != 0 and counter != 0 and hantei ):
      counter -=1
   return counter

def modelAnswer():
   tmp=1
def main():
   N,x = map(int,input().split())
   A = list(map(int,input().split()))
   print(myAnswer(N,x,A[:]))


if __name__ == '__main__':
   main()
