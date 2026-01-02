'''
difficult   　: 
ペナルティ　  　:分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''
from operator import mul
def myAnswer(B:list,A:list,C:int) -> int:
   counter=0
   for a in A:
      if( sum(map(mul,B,a)) + C > 0):
         counter += 1
   return counter




def modelAnswer():
   tmp=1
def main():
   N,M,C = map(int,input().split())
   B = list(map(int,input().split()))
   A=[]
   for _ in range(N):
      A.append(list(map(int,input().split())))
      
   ans = myAnswer(B[:],A[:],C)
   print((ans))


if __name__ == '__main__':
   main()