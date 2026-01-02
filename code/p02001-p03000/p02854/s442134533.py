from itertools import accumulate
def myAnswer(N:int,A:list) -> int:
   accum = [A[0]]
   accumRev = [sum(A)]
   ans = 10**10
   for i in range(1,N):
      accumRev.append(accumRev[-1] - A[i-1])
      accum.append(accum[-1]+A[i])
   for i in range(len(accum)-1):
      ans = min(ans,abs(accumRev[i+1] - accum[i]))
   return ans
      
def modelAnswer(N:int,A:list) -> int:
   T1 = [A[0]]
   T2 = [sum(A)]
   for i in range(1,N): # O(N)
      T1.append(T1[-1]+A[i])
      T2.append(T2[0] - T1[i-1])
   # print(T1,T2)
   ans = 10**10
   for i in range(len(T1)-1): # O(N/2)
      # print(abs(T1[i]-T2[i+1]))
      ans = min(ans,abs(T1[i]-T2[i+1]))
   return ans


def main():
   N = int(input())
   A = list(map(int,input().split()))
   # print(modelAnswer(N,A[:]))
   # print("-----------------------------")
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()
