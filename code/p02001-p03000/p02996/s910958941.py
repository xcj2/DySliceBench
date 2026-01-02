
def myAnswer(N:int,A:list,B:list) -> str:
   dic = {}
   for a,b in  zip(A,B):
      if(b in dic.keys()):
         dic[b].append(a)
      else:
         dic[b] = [a]
   now = 0
   dic = sorted(dic.items())
   for deadline,time in dic:
      time.sort()
      # print(deadline,time)
      for t in time:
         if(deadline < now + t):
            return "No"
         now += t
   return "Yes"

def modelAnswer():
   return
def main():
   N = int(input())
   A = []
   B = []
   for _ in range(N):
      a,b = map(int,input().split())
      A.append(a)
      B.append(b)
   print(myAnswer(N,A,B))
if __name__ == '__main__':
   main()