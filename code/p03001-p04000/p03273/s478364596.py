def myAnswer(H:int,W:int,A:list) -> None:
   ans = []
   for a in A:
      for i in a:
         if(i == "#"):
            ans.append(a)
            break
         
   ansT = list(zip(*ans))
   ans = []
   for t in ansT:
      for i in t:
         if(i == "#"):
            ans.append(t)
            break
   ans = list(zip(*ans))
   for a in ans:
      string = ""
      for i in a:
         string +=i
      print(string)


def modelAnswer():
   return
def main():
   H,W = map(int,input().split())
   A = []
   for _ in range(H):
      A.append(list(input()))
   myAnswer(H,W,A[:])
if __name__ == '__main__':
   main()