def myAnswer(N:int,A:int,B:int) -> int:
   ans = 0
   BN = N - B
   A1 = A - 1
   while True:
      if((B - A) % 2== 0):
         ans += (B - A)//2
         break
      elif(A == 1):
         ans += 1
         B -= 1
      elif(B == N):
         ans += 1
         A += 1
      else:
         if(BN > A1):
            ans +=A1
            B -= A1
            A = 1
         else:
            ans += BN
            A += BN
            B = N
   return ans

def modelAnswer():
   tmp=1
def main():
   N,A,B = map(int,input().split())
   print(myAnswer(N,A,B))
if __name__ == '__main__':
   main()