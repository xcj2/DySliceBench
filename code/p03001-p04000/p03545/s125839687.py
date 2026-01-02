from itertools import permutations
def myAnswer(ABCD:list) -> str:
   ans = ""
   l = ["+","+","+","-","-","-"]
   # l = ["+","-"]
   for c in permutations(l,3):
      total = int(ABCD[0])
      ans = ABCD[0]
      for n,i in enumerate(c):
         if(i=="+"):
            total += int(ABCD[n+1])
            ans += "+" + ABCD[n+1]
         else:
            total -= int(ABCD[n+1])
            ans += "-" + ABCD[n+1]
      if(total == 7):
         return ans + "=7"




def modelAnswer():
   tmp=1
def main():
   ABCD = list(input())
   print(myAnswer(ABCD[:]))

if __name__ == '__main__':
   main()