from collections import Counter
def myAnswer(N:int,S:list) -> int:
   dic = []
   for s in S:
      dic.append(Counter(s))
   ans = dic.pop(0)
   for d in dic:
      key = set(ans.keys()) - (set(d.keys()) & set(ans.keys()))
      for k in key:
         del ans[k]
      for key,value in d.items():
         if(key in ans.keys()):
            ans[key] = min(value,ans[key])
   result = ""
   for alph,counter in sorted(ans.items()):
      result += alph * counter
   return result

def modelAnswer():
   return
def main():
   N = int(input())
   S = [list(input()) for _ in range(N)]
   print(myAnswer(N,S[:]))
if __name__ == '__main__':
   main()