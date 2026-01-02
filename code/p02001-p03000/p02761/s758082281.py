
def myAnswer(N:int,M:int,S:list,C:list)-> int:
   ans=-1
   for i in range(10**N):
      if(len(str(i)) == N):
          for s,c in zip(S,C):
              tmp=list(str(i))
              if(tmp[s-1] != str(c)):
                  break
          else:
              if(ans == -1):
                  ans=i
              else:
                ans=min(ans,i)
   return ans
def modelAnswer():
   return
def main():
   N,M = map(int,input().split())
   S= []
   C = []
   for _ in range(M):
      s,c =map(int,input().split())
      S.append(s)
      C.append(c)
   print(myAnswer(N,M,S[:],C[:]))

if __name__ == '__main__':
   main()


