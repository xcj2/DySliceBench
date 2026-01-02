import itertools
def func(n,j):
   if(n % 10 == 0 or j==4):
      return n
   return n //10 * 10 + 10
def myAnswer(A:int,B:int,C:int,D:int,E:int) -> int:
   dishes = [A,B,C,D,E]
   ans = 10**9
   for i in itertools.permutations(dishes):
      total = 0
      for j,a in enumerate(i):
         total+= func(a,j)
      ans = min(total,ans)
   return ans


def modelAnswer():
   tmp=1
def main():
   A = int(input())
   B = int(input())
   C = int(input())
   D = int(input())
   E = int(input())
   print(myAnswer(A,B,C,D,E))

if __name__ == '__main__':
   main()