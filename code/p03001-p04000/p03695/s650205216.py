def myAnswer(N:int,A:list) -> int:
   counter = 0
   free = 0
   rate = [0 for _ in range(8)]
   for a in A:
      if(a <= 399):
         rate[0] += 1
      elif(a <= 799):
         rate [1] += 1
      elif(a <= 1199):
         rate[2] += 1
      elif(a <= 1599):
         rate[3] += 1
      elif(a <= 1999):
         rate[4] += 1
      elif(a <= 2399):
         rate[5] += 1
      elif(a <= 2799):
         rate[6] += 1
      elif(a <= 3199):
         rate[7] += 1
      else:
         free += 1
   for r in rate:
      if(r > 0):
         counter += 1
   if(free == N):
      print(1,free)
   else:
      print(counter,counter+free)


def modelAnswer():
   return
def main():
   N = int(input())
   A = list(map(int,input().split()))
   myAnswer(N,A[:])
if __name__ == '__main__':
   main()