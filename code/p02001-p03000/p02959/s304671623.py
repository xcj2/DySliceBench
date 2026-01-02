def myAnswer(N:int,A:list,B:list) -> int:
   total = 0
   for i in range(N):
      if(A[i] < B [i]):
         total += A[i]
         if(A[i + 1] > B[i] - A[i]):
            A[i+1] -= B[i] - A[i]
            total += B[i] - A[i]
         else:
            total += A[i + 1]
            A[i + 1] = 0
         A[i] = 0
      else:
         A[i] -= B[i]
         total += B[i]
   return total

def modelAnswer():
   tmp=1
def main():
   N = int(input())
   A = list(map(int,input().split()))
   B = list(map(int,input().split()))
   print(myAnswer(N,A[:],B[:]))

if __name__ == '__main__':
   main()