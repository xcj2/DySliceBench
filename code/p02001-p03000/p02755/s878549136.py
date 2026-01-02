from math import floor,ceil
# 自分の解答(模範解答と同じ)
def myAnswer(A:int,B:int) -> int:
   price = 1
   while True:
      if(floor(price*0.08)==A and floor(price*0.1)==B):
         return price
      elif(floor(price*0.08)>A or floor(price*0.1)>B):
         return -1
      else:
         price+=1
   

def modelAnswer(A:int,B:int) -> int:
   ans = max(ceil(A/0.08),ceil(B/0.1))
   return ans if(floor(ans*0.08)==A and floor(ans*0.1)==B) else -1

def main():
   A,B = map(int,input().split())
   print(modelAnswer(A,B))

if __name__ == '__main__':
   main()