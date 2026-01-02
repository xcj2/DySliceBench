
def myAnswer(N:int,M:int,p:list,S:list) -> None:
   ac = 0
   wa = 0
   dic = {}
   for key,value in zip(p,S):
      if(key in dic.keys()):
         dic[key].append(value)
      else:
         dic[key] = [value]
   for values in dic.values():
      if(("AC" in values)):
         for v in values:
            if(v == "AC"):
               ac+=1
               break
            else:
               wa+=1
   print(ac,wa)

def modelAnswer():
   tmp=1
def main():
   N, M = map(int,input().split())
   p =[]
   S = []
   for _ in range(M):
      tmp = list(map(str,input().split()))
      p.append(tmp[0])
      S.append(tmp[1])
   myAnswer(N,M,p[:],S[:])
if __name__ == '__main__':
   main()
