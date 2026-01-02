def myAnswer(N:int,M:int,A:list,B:list) -> int:
   dic ={}
   for i in range(N):
      if(A[i] in dic.keys()):
         dic[A[i]] += B[i]
      else:
         dic[A[i]] = B[i]
   dic2 = sorted(dic.items())
   total = 0
   for key,value in dic2:
      if(M - value < 0):
         total += M * key
         break
      else:
         total += key * value
         M -= value
   return total

def modelAnswer():
   tmp=1
def main():
   N,M = map(int,input().split())
   A = []
   B = []
   for _ in range(N):
      a,b=map(int,input().split())
      A.append(a)
      B.append(b)
   print(myAnswer(N,M,A[:],B[:]))
if __name__ == '__main__':
   main()