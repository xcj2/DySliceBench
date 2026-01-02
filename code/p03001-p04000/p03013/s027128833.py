'''
Accepted    　:No
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''
import itertools


def myAnswer(N:int,M:int,A:list) -> int:
   safe_stairs =[True] * (N + 1)
   mod = 10**9 + 7
   for a in A:
      safe_stairs[a] = False

   DP = [0] * (N+1)
   DP[0] = 1
   if safe_stairs[1]:DP[1] = 1

   for n in range(2,N + 1):
      if safe_stairs[n - 1]:
         DP[n] += DP[n - 1]
      if safe_stairs[n - 2]:
         DP[n] += DP[n - 2]
      DP[n] %= mod

   return DP[N]
      



def modelAnswer():
   return
def main():
   N,M = map(int,input().split())
   A = [int(input()) for _ in range(M)]
   print(myAnswer(N,M,A))

if __name__ == '__main__':
   main()

