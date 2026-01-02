
def myAnswer(N:int,K:int,A:list) -> int:
   kinds = 0
   dic = {}
   for a in A:
      if(a in dic.keys()):
         dic[a]+=1
      else:
         dic[a]=1
         kinds +=1
   if(kinds <= K):return 0
   sub = kinds - K
   ans = 0
   dic2 = sorted(dic.items(), key=lambda x:x[1])
   for key,value in dic2:
      if(sub == 0):
         break
      else:
         ans += value
         sub -= 1
   return ans

def modelAnswer():
   return
def main():
   N,K = map(int,input().split())
   A = list(map(int,input().split()))
   print(myAnswer(N,K,A[:]))
if __name__ == '__main__':
   main()