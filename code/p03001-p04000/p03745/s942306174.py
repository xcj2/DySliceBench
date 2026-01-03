def myAnswer(N:int,A:list) -> int:
   if(N == 1): return 1
   pre = A.pop(0)
   counter = 1
   state = 0 # 0:どちらでもない状態、1:単調非減少、2:単調非増加
   for a in A:
      if(pre == a):
         pre = a
         continue
      if(state == 0):
         if(pre < a):
            state = 1
         else:
            state = 2
      elif(pre < a and state == 2):
         counter += 1
         state = 0
      elif(pre > a and state == 1):
         counter += 1
         state = 0
      pre = a
   return counter

def modelAnswer():
   return
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()