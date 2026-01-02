'''
Accepted    　:No
difficult   　: 
ペナルティ　  　:5分
実際の回答時間  :分
WAの回数　     :回
合計時間　　  　:分
'''

def myAnswer(N:int,A:list,B:list) -> int:
   negative = []
   positive = []
   counter = 0
   total = 0
   for a,b in zip(A,B):
      if(a - b < 0):
         negative.append(a - b)
      else:
         positive.append(a - b)
   negative.sort()
   positive.sort(reverse=True)
   for d in negative + positive:
      if(d >= 0 and total >= 0):
         break
      else:
         total += d
         counter += 1
   
   return counter if(total >= 0) else -1

def modelAnswer():
   return
def main():
   N = int(input())
   A = list(map(int,input().split()))
   B = list(map(int,input().split()))
   print(myAnswer(N,A,B))

if __name__ == '__main__':
   main()