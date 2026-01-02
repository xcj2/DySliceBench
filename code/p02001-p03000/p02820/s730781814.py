
def myAnswer(N:int,K:int,R:int,S:int,P:int,T:str) -> int:
   dic = {"r":R,"s":S,"p":P}
   dic2 = {"r":["p","-"],"s":["r","-"],"p":["s","-"]}
   total = 0
   ans = []
   for n in range(N):
      target = T[n]
      if(n  < K):
         ans.append(dic2[target][0])
         total += dic[dic2[target][0]]
      else:
         if(ans[n - K] == dic2[target][0]):
            ans.append(dic2[target][1])
         else:
            ans.append(dic2[target][0])
            total += dic[dic2[target][0]]
   return total

def modelAnswer():
   return
def main():
   N,K = map(int,input().split())
   R,S,P = map(int,input().split())
   T = input()
   print(myAnswer(N,K,R,S,P,T))
if __name__ == '__main__':
   main()