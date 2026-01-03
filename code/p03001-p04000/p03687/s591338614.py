def myAnswer(s:list) -> int:
   setS = set(s)
   if(len(setS) == 1): return 0
   ans = 10**9
   while len(setS) != 0:
      target = setS.pop()
      counter = 0
      tmp = s[:]
      while True:
         pre = tmp.pop(0)
         N = len(tmp)
         for i in range(N):
            now = tmp.pop(0)
            if(pre == target or now==target):
               tmp.append(target)
            else:
               tmp.append(now)
            pre = now
         counter += 1
         if(len(set(tmp))==1):
            break
      ans = min(ans,counter)
   return ans



def modelAnswer():
   return
def main():
   s = list(input())
   print(myAnswer(s[:]))
if __name__ == '__main__':
   main()