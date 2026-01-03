def myAnswer(N:int,A:list) -> int:
   dic = {}
   for a in A:
      if(a in dic.keys()):
         dic[a]+=1
      else:
         dic[a] = 1
   ans = []
   for key,value in dic.items():
      if(value >= 4):
         ans.append(key)
         ans.append(key)
      elif(value >= 2):
         ans.append(key)
   if(len(ans) <= 1):
      return 0
   ans.sort(reverse = True)
   return ans[0]*ans[1]

def modelAnswer():
   return
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()