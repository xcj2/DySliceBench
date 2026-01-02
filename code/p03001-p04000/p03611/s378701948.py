def myAnswer(N:int,A:list) -> int:
   if(N == 1): return 1
   dic ={}
   for a in A:
      if(a == 0):
         for i in range(2):
            if(i in dic.keys()):
               dic[i]+=1
            else:
               dic[i]=1
      else:
         for i in range(a-1,a+2):
            if(i in dic.keys()):
               dic[i]+=1
            else:
               dic[i] = 1
   return max(list(dic.values()))

def modelAnswer():
   return
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()