def myAnswer(N:int,s:list,M:int,t:list) -> int:
   dic = dict()
   for blueCard in s:
      if(blueCard in dic.keys()):
         dic[blueCard]+=1
      else:
         dic[blueCard]=1
   for redCard in t:
      if(redCard in dic.keys()):
         if(dic[redCard] > 0):
            dic[redCard] -= 1
   return max(dic.values())


def modelAnswer():
   tmp=1
def main():
   N = int(input())
   s = [input() for _ in range(N)]
   M = int(input())
   t = [input() for _ in range(M)]
   print(myAnswer(N,s[:],M,t[:]))
if __name__ == '__main__':
   main()