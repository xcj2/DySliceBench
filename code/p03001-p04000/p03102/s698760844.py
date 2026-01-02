from operator import mul

# 自分の解答
def myAnswer(B:list,A:list,C:int) -> int:
   counter=0
   for a in A:
      if( sum(map(mul,B,a)) + C > 0): counter += 1
   return counter


def modelAnswer(B:list,A:list,C:int,N:int,M:int) -> int:
   ans = 0
   for i in range(N):
      total = 0
      for j in range(M):
         total += A[i][j] * B[j]
      if(total + C > 0): ans += 1
   return ans


def main():
   N,M,C = map(int,input().split())
   B = list(map(int,input().split()))
   A=[]
   for _ in range(N):
      A.append(list(map(int,input().split())))

   ans = myAnswer(B[:],A[:],C)
   ans2 = modelAnswer(B[:],A[:],C,N,M)
   print(ans2)


if __name__ == '__main__':
   main()